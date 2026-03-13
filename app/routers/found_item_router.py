from fastapi import APIRouter, Depends
from app.controllers.found_item_controller import (
    get_all_items,
    get_item,
    create_item,
    update_item,
    delete_item,
)
from app.dependencies.auth_dependency import require_auth, require_admin

router = APIRouter(prefix="/items", tags=["Found Items"])

# Public routes
router.add_api_route("/", get_all_items, methods=["GET"])
router.add_api_route("/{item_id}", get_item, methods=["GET"])

# Protected routes
router.add_api_route("/", create_item, methods=["POST"], status_code=201, dependencies=[Depends(require_auth)])
router.add_api_route("/{item_id}", update_item, methods=["PUT"], dependencies=[Depends(require_auth)])
router.add_api_route("/{item_id}", delete_item, methods=["DELETE"], dependencies=[Depends(require_auth)])