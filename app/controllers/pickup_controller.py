from fastapi import Depends, HTTPException
from app.schemas.pickup_schema import PickupLogResponse, PickupLogResponse
from app.services.pickup_service import PickupLogService
from app.dependencies.pickup_dependency import get_pickup_service
from app.dependencies.auth_dependency import require_admin

from typing import Any

def get_all_pickups(
    _: dict = Depends(require_admin),
    service: PickupLogService = Depends(get_pickup_service),
):
    """Get all pickup logs. Admin only."""
    return service.get_all()


def get_pickup(
    log_id: int,
    _: dict = Depends(require_admin),
    service: PickupLogService = Depends(get_pickup_service),
):
    """Get a pickup log by ID. Admin only."""
    try:
        return service.get_by_id(log_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def create_pickup(
    payload: Any,
    _: dict = Depends(require_admin),
    service: PickupLogService = Depends(get_pickup_service),
):
    """Log an item pickup. Admin only."""
    try:
        return service.create(
            claim_request_id=payload.claim_request_id,
            claimant_id=payload.claimant_id,
            picked_up_at=payload.picked_up_at,
            verified_by_admin_id=payload.verified_by_admin_id,
            counter_number=payload.counter_number,
            pickup_code=payload.pickup_code,
            remarks=payload.remarks,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))