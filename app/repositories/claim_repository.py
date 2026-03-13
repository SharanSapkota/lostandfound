from sqlalchemy.orm import Session
from app.models.claim import ClaimRequest

class ClaimRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, claim_id: int) -> ClaimRequest | None:
        return self.db.query(ClaimRequest).filter(ClaimRequest.id == claim_id).first()

    def get_by_item_id(self, item_id: int) -> list[ClaimRequest]:
        return self.db.query(ClaimRequest).filter(ClaimRequest.item_id == item_id).all()

    def get_by_claimant_id(self, claimant_id: int) -> list[ClaimRequest]:
        return self.db.query(ClaimRequest).filter(ClaimRequest.claimant_id == claimant_id).all()

    def get_existing_claim(self, item_id: int, claimant_id: int) -> ClaimRequest | None:
        return self.db.query(ClaimRequest).filter(
            ClaimRequest.item_id == item_id,
            ClaimRequest.claimant_id == claimant_id
        ).first()

    def create(self, claim: ClaimRequest) -> ClaimRequest:
        self.db.add(claim)
        self.db.commit()
        self.db.refresh(claim)
        return claim

    def update(self, claim: ClaimRequest) -> ClaimRequest:
        self.db.commit()
        self.db.refresh(claim)
        return claim

    def delete(self, claim: ClaimRequest) -> None:
        self.db.delete(claim)
        self.db.commit()