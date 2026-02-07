from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ClaimRequestCreate(BaseModel):
    item_id: int
    proof_details: str
    proof_image_url: Optional[str] = None


class ClaimApprove(BaseModel):
    admin_note: Optional[str] = None
    counter_number: Optional[str] = None


class ClaimRequestResponse(BaseModel):
    id: int
    item_id: int
    claimant_id: int
    status: str
    admin_note: Optional[str]
    pickup_code: Optional[str]
    counter_number: Optional[str]
    approved_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True
