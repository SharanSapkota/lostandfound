from sqlalchemy.orm import Session
from app.models.found_item import FoundItem

class UserFoundRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: int) -> FoundItem | None:
        return self.db.query(FoundItem).filter(FoundItem.id == id).first()

    def create(self, found_item: FoundItem) -> FoundItem:
        self.db.add(found_item)
        self.db.commit()
        self.db.refresh(found_item)
        return found_item

    def update(self, found_item: FoundItem) -> FoundItem:
        self.db.commit()
        self.db.refresh(found_item)
        return found_item

    