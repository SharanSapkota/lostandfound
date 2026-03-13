# app/controllers/foundItemController.py

from fastapi import Depends, HTTPException
from app.schemas.found_item_schema import FoundItemCreate, FoundItemUpdate, FoundItemResponse
from app.services.found_item_service import FoundItemService
from app.dependencies.found_item_dependency import get_item_service
from app.dependencies.auth_dependency import require_auth


def get_all_items(
    service: FoundItemService = Depends(get_item_service),
):
    """Get all found items. Public."""
    return service.get_all()


def get_item(
    item_id: int,
    service: FoundItemService = Depends(get_item_service),
):
    """Get a found item by ID. Public."""
    try:
        return service.get_by_id(item_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def create_item(
    payload: FoundItemCreate,
    current_user: dict = Depends(require_auth),
    service: FoundItemService = Depends(get_item_service),
):
    """Report a new found item. Requires login."""
    return service.create(
        reported_by=current_user["user_id"],
        title=payload.title,
        description=payload.description,
        category=payload.category,
        location_found=payload.location_found,
        date_found=payload.date_found,
        image_url=payload.image_url,
    )


def update_item(
    item_id: int,
    payload: FoundItemUpdate,
    current_user: dict = Depends(require_auth),
    service: FoundItemService = Depends(get_item_service),
):
    """Update a found item. Must be the reporter or admin."""
    try:
        item = service.get_by_id(item_id)
        if item.reported_by != current_user["user_id"] and current_user.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Forbidden")
        return service.update(item_id, **payload.model_dump(exclude_none=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def delete_item(
    item_id: int,
    current_user: dict = Depends(require_auth),
    service: FoundItemService = Depends(get_item_service),
):
    """Delete a found item. Must be the reporter or admin."""
    try:
        item = service.get_by_id(item_id)
        if item.reported_by != current_user["user_id"] and current_user.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Forbidden")
        service.delete(item_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))