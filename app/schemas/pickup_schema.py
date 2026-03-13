from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PickupLogResponse(BaseModel):
    id: int
    claim_request_id: int
    item_id: int
    claimant_id: int
    verified_by_admin_id: Optional[int]
    counter_number: Optional[str]
    pickup_code: Optional[str]
    picked_up_at: datetime
    remarks: Optional[str]

    class Config:
        from_attributes = True
