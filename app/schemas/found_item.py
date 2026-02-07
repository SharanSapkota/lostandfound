from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FoundItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    location_found: Optional[str] = None
    date_found: Optional[datetime] = None
    image_url: Optional[str] = None


class FoundItemResponse(FoundItemCreate):
    id: int
    status: str
    reported_by: int
    created_at: datetime

    class Config:
        from_attributes = True
