from app.repositories.claim_repository import ClaimRepository
from app.repositories.found_item_repository import FoundItemRepository
from app.schemas.claim_schema import ClaimRequestResponse, ClaimRequestCreate
from datetime import datetime

class ClaimService:
    def __init__(self, repo: ClaimRepository, item_repo: FoundItemRepository):
        self.repo = repo
        self.item_repo = item_repo

    def get_by_item(self, item_id: int) -> list[ClaimRequestResponse]:
        item = self.item_repo.get_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        return self.repo.get_by_item_id(item_id)

    def get_by_id(self, claim_id: int) -> ClaimRequestResponse:
        claim = self.repo.get_by_id(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        return claim

    def create(self, item_id: int, claimant_id: int, proof_details: str, proof_image_url: str = None) -> ClaimRequestCreate:
        item = self.item_repo.get_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        if item.status != "available":
            raise ValueError("Item is not available for claiming")

        existing = self.repo.get_existing_claim(item_id, claimant_id)
        if existing:
            raise ValueError("You have already submitted a claim for this item")

        claim = ClaimRequestCreate(
            item_id=item_id,
            claimant_id=claimant_id,
            proof_details=proof_details,
            proof_image_url=proof_image_url,
        )
        return self.repo.create(claim)

    def update(self, claim_id: int, admin_id: int, status: str,
               admin_note: str = None, pickup_code: str = None, counter_number: str = None) -> ClaimRequestCreate:
        claim = self.repo.get_by_id(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        if claim.status in ("approved", "rejected", "cancelled"):
            raise ValueError(f"Claim is already {claim.status}")

        claim.status = status
        claim.admin_id = admin_id
        claim.admin_note = admin_note
        claim.pickup_code = pickup_code
        claim.counter_number = counter_number
        if status == "approved":
            claim.approved_at = datetime.utcnow()
            # mark item as claimed
            item = self.item_repo.get_by_id(claim.item_id)
            if item:
                item.status = "claimed"
                self.item_repo.update(item)

        return self.repo.update(claim)

    def delete(self, claim_id: int) -> None:
        claim = self.repo.get_by_id(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        self.repo.delete(claim)
