
from fastapi import Depends, HTTPException
from app.schemas.claim_schema import ClaimRequestCreate, ClaimRequestResponse
from app.services.claim_service import ClaimService
from app.dependencies.claim_dependency import get_claim_service
from app.dependencies.auth_dependency import require_auth, require_admin


def get_claims_for_item(
    item_id: int,
    _: dict = Depends(require_admin),
    service: ClaimService = Depends(get_claim_service),
):
    """Get all claims for an item. Admin only."""
    try:
        return service.get_by_item(item_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def create_claim(
    item_id: int,
    payload: ClaimRequestCreate,
    current_user: dict = Depends(require_auth),
    service: ClaimService = Depends(get_claim_service),
):
    """Submit a claim for a found item. Requires login."""
    try:
        return service.create(
            item_id=item_id,
            claimant_id=current_user["user_id"],
            proof_details=payload.proof_details,
            proof_image_url=payload.proof_image_url,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


def get_claim(
    claim_id: int,
    current_user: dict = Depends(require_auth),
    service: ClaimService = Depends(get_claim_service),
):
    """Get a claim by ID. Must be the claimant or admin."""
    try:
        claim = service.get_by_id(claim_id)
        if claim.claimant_id != current_user["user_id"] and current_user.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Forbidden")
        return claim
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def update_claim(
    claim_id: int,
    payload: ClaimRequestCreate,
    current_user: dict = Depends(require_admin),
    service: ClaimService = Depends(get_claim_service),
):
    """Approve, reject or cancel a claim. Admin only."""
    try:
        return service.update(
            claim_id=claim_id,
            admin_id=current_user["user_id"],
            status=payload.status,
            admin_note=payload.admin_note,
            pickup_code=payload.pickup_code,
            counter_number=payload.counter_number,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


def delete_claim(
    claim_id: int,
    current_user: dict = Depends(require_auth),
    service: ClaimService = Depends(get_claim_service),
):
    """Delete a claim. Must be the claimant or admin."""
    try:
        claim = service.get_by_id(claim_id)
        if claim.claimant_id != current_user["user_id"] and current_user.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Forbidden")
        service.delete(claim_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))