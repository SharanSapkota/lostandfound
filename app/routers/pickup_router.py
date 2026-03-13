# app/routers/pickupRouter.py

from fastapi import APIRouter, Depends
from lostAndFound.app.controllers.pickup_controller import (
    get_all_pickups,
    get_pickup,
    create_pickup,
)
from lostAndFound.app.dependencies.auth_dependency import require_admin

router = APIRouter(prefix="/pickups", tags=["Pickup Logs"])

# All pickup routes are admin only
router.add_api_route("/", get_all_pickups, methods=["GET"], dependencies=[Depends(require_admin)])
router.add_api_route("/{log_id}", get_pickup, methods=["GET"], dependencies=[Depends(require_admin)])
router.add_api_route("/", create_pickup, methods=["POST"], status_code=201, dependencies=[Depends(require_admin)])