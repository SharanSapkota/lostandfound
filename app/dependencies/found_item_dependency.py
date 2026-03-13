
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.found_item_repository import FoundItemRepository
from app.services.found_item_service import FoundItemService

def get_item_service(db: Session = Depends(get_db)) -> FoundItemService:
    found_item_repository = FoundItemRepository(db)
    return FoundItemService(found_item_repository)