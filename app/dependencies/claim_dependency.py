
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.claim_repository import ClaimRepository
from app.repositories.found_item_repository import FoundItemRepository
from app.services.claim_service import ClaimService


def get_claim_service(db: Session = Depends(get_db)) -> ClaimService:
    claim_repository = ClaimRepository(db)
    found_item_repository = FoundItemRepository(db)
    return ClaimService(claim_repository, found_item_repository)