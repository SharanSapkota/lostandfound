from app.repositories.found_item_repository import FoundItemRepository
from app.schemas.found_item_schema import FoundItemResponse 
from datetime import datetime

class FoundItemService:
    def __init__(self, repo: FoundItemRepository):
        self.repo = repo

    def get_all(self) -> list[FoundItemResponse]:
        return self.repo.get_all()

    def get_by_id(self, item_id: int) -> FoundItemResponse:
        item = self.repo.get_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        return item

    def create(self, reported_by: int, title: str, description: str = None,
               category: str = None, location_found: str = None,
               date_found: datetime = None, image_url: str = None) -> FoundItemResponse:
        item = FoundItemResponse(
            title=title,
            description=description,
            category=category,
            location_found=location_found,
            date_found=date_found,
            image_url=image_url,
            reported_by=reported_by,
        )
        return self.repo.create(item)

    def update(self, item_id: int, **kwargs) -> FoundItemResponse:
        item = self.repo.get_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        for key, value in kwargs.items():
            if value is not None:
                setattr(item, key, value)
        return self.repo.update(item)

    def delete(self, item_id: int) -> None:
        item = self.repo.get_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        self.repo.delete(item)
