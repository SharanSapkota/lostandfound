from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class PickupLog(Base):
    __tablename__ = "pickup_logs"

    id = Column(Integer, primary_key=True, index=True)

    claim_request_id = Column(
        Integer,
        ForeignKey("claim_requests.id"),
        nullable=False,
        unique=True,
        ondelete="CASCADE"
    )

    claimant_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    verified_by_admin_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    counter_number = Column(String, nullable=True)
    pickup_code = Column(String, nullable=True)
    picked_up_at = Column(DateTime, nullable=False)
    remarks = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    claim_request = relationship(
        "ClaimRequest",
        back_populates="pickup_log"
    )

    claimant = relationship("User", foreign_keys=[claimant_id])
    verified_by_admin = relationship("User", foreign_keys=[verified_by_admin_id])
