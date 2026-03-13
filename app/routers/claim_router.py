
from fastapi import APIRouter, Depends
from app.controllers.claim_controller import (
    get_claims_for_item,
    get_claim,
    create_claim,
    update_claim,
    delete_claim,
)
from app.dependencies.auth_dependency import require_auth, require_admin

router = APIRouter(tags=["Claims"])

# Nested under /items/{item_id}/claims
router.add_api_route("/items/{item_id}/claims", get_claims_for_item, methods=["GET"], dependencies=[Depends(require_admin)])
router.add_api_route("/items/{item_id}/claims", create_claim, methods=["POST"], status_code=201, dependencies=[Depends(require_auth)])

# Standalone /claims/{claim_id}
router.add_api_route("/claims/{claim_id}", get_claim, methods=["GET"], dependencies=[Depends(require_auth)])
router.add_api_route("/claims/{claim_id}", update_claim, methods=["PUT"], dependencies=[Depends(require_admin)])
router.add_api_route("/claims/{claim_id}", delete_claim, methods=["DELETE"], dependencies=[Depends(require_auth)])