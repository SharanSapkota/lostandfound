from sqlalchemy.orm import Session
from app.models.found_item import FoundItem

class FoundItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, item_id: int) -> FoundItem | None:
        return self.db.query(FoundItem).filter(FoundItem.id == item_id).first()

    def get_all(self) -> list[FoundItem]:
        return self.db.query(FoundItem).all()

    def create(self, item: FoundItem) -> FoundItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: FoundItem) -> FoundItem:
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item: FoundItem) -> None:
        self.db.delete(item)
        self.db.commit()
