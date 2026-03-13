from sqlalchemy.orm import Session
from app.models.pickup_log import PickupLog

class PickupLogRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, log_id: int) -> PickupLog | None:
        return self.db.query(PickupLog).filter(PickupLog.id == log_id).first()

    def get_all(self) -> list[PickupLog]:
        return self.db.query(PickupLog).all()

    def get_by_claim_id(self, claim_id: int) -> PickupLog | None:
        return self.db.query(PickupLog).filter(PickupLog.claim_request_id == claim_id).first()

    def create(self, log: PickupLog) -> PickupLog:
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log
