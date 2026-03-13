from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class ClaimRequest(Base):
    __tablename__ = "claim_requests"

    id = Column(Integer, primary_key=True, index=True)

    item_id = Column(Integer, ForeignKey("found_items.id"), nullable=False)

    claimant_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    proof_details = Column(String, nullable=False)
    proof_image_url = Column(String, nullable=True)

    status = Column(String, default="pending")
    # pending | approved | rejected | cancelled

    admin_note = Column(String, nullable=True)
    pickup_code = Column(String, nullable=True)
    counter_number = Column(String, nullable=True)
    approved_at = Column(DateTime, nullable=True)

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

    pickup_log = relationship("PickupLog", back_populates="claim_request", uselist=False)
