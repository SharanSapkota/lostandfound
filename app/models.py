from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    firstName = Column(String)
    lastName = Column(String)
    password_hash = Column(String, nullable=False)
    phone = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    found_items = relationship("FoundItem", back_populates="user")

    claims_made = relationship(
        "ClaimRequest",
        foreign_keys="ClaimRequest.claimant_id",
        back_populates="claimant"
    )

    claims_reviewed = relationship(
        "ClaimRequest",
        foreign_keys="ClaimRequest.admin_id",
        back_populates="admin"
    )


class FoundItem(Base):
    __tablename__ = "found_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    location_found = Column(String)
    date_found = Column(DateTime)
    image_url = Column(String)
    status = Column(String, default="available")

    reported_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="found_items")

    claim_requests = relationship(
        "ClaimRequest",
        back_populates="item"
    )


class ClaimRequest(Base):
    __tablename__ = "claim_requests"

    id = Column(Integer, primary_key=True, index=True)

    item_id = Column(Integer, ForeignKey("found_items.id"), nullable=False)
    claimant_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    admin_id = Column(Integer, ForeignKey("users.id"))

    proof_details = Column(String, nullable=False)
    proof_image_url = Column(String)
    status = Column(String, default="pending")

    admin_note = Column(String)
    pickup_code = Column(String)
    approved_at = Column(DateTime)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    item = relationship("FoundItem", back_populates="claim_requests")

    claimant = relationship(
        "User",
        foreign_keys=[claimant_id],
        back_populates="claims_made"
    )

    admin = relationship(
        "User",
        foreign_keys=[admin_id],
        back_populates="claims_reviewed"
    )

    pickup_log = relationship(
        "PickupLog",
        back_populates="claim_request",
        uselist=False
    )


class PickupLog(Base):
    __tablename__ = "pickup_logs"

    id = Column(Integer, primary_key=True, index=True)

    claim_request_id = Column(
        Integer,
        ForeignKey("claim_requests.id"),
        nullable=False,
        unique=True
    )

    item_id = Column(Integer, ForeignKey("found_items.id"), nullable=False)
    claimant_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    verified_by_admin_id = Column(Integer, ForeignKey("users.id"))

    counter_number = Column(String)
    pickup_code = Column(String)
    picked_up_at = Column(DateTime, nullable=False)
    remarks = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    claim_request = relationship("ClaimRequest", back_populates="pickup_log")
    item = relationship("FoundItem")

    claimant = relationship(
        "User",
        foreign_keys=[claimant_id]
    )

    verified_by_admin = relationship(
        "User",
        foreign_keys=[verified_by_admin_id]
    )
