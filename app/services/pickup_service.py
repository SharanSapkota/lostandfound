from datetime import datetime

from app.models.pickup_log import PickupLog
from app.repositories.claim_repository import ClaimRepository
from app.repositories.pickup_repository import PickupLogRepository


class PickupLogService:
    def __init__(self, repo: PickupLogRepository, claim_repo: ClaimRepository):
        self.repo = repo
        self.claim_repo = claim_repo

    def get_all(self) -> list[PickupLog]:
        return self.repo.get_all()

    def get_by_id(self, log_id: int) -> PickupLog:
        log = self.repo.get_by_id(log_id)
        if not log:
            raise ValueError("Pickup log not found")
        return log

    def create(self, claim_request_id: int, claimant_id: int, picked_up_at: datetime,
               verified_by_admin_id: int = None, counter_number: str = None,
               pickup_code: str = None, remarks: str = None) -> PickupLog:

        claim = self.claim_repo.get_by_id(claim_request_id)
        if not claim:
            raise ValueError("Claim not found")
        if claim.status != "approved":
            raise ValueError("Claim must be approved before logging pickup")

        existing = self.repo.get_by_claim_id(claim_request_id)
        if existing:
            raise ValueError("Pickup log already exists for this claim")

        log = PickupLog(
            claim_request_id=claim_request_id,
            claimant_id=claimant_id,
            verified_by_admin_id=verified_by_admin_id,
            counter_number=counter_number,
            pickup_code=pickup_code,
            picked_up_at=picked_up_at,
            remarks=remarks,
        )
        return self.repo.create(log)
