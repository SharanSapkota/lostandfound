from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    firstName: str
    lastName: str
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True



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



class ClaimRequestCreate(BaseModel):
    item_id: int
    proof_details: str
    proof_image_url: Optional[str] = None


class ClaimRequestResponse(BaseModel):
    id: int
    item_id: int
    claimant_id: int
    status: str
    admin_note: Optional[str]
    pickup_code: Optional[str]
    approved_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True



class ClaimApprove(BaseModel):
    admin_note: Optional[str] = None


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
