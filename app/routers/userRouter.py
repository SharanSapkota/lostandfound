from fastapi import APIRouter, Depends
from app.controllers.userController import (
    register,
    login,
    get_all_users,
    get_user,
    update_user,
    delete_user,
)
from app.dependencies.authDependency import require_auth, require_admin

router = APIRouter(prefix="/users", tags=["Users"])

router.add_api_route("/register", register, methods=["POST"], status_code=201)
router.add_api_route("/login", login, methods=["POST"])

router.add_api_route("/", get_all_users, methods=["GET"], dependencies=[Depends(require_admin)])
router.add_api_route("/{user_id}", get_user, methods=["GET"], dependencies=[Depends(require_auth)])
router.add_api_route("/{user_id}", update_user, methods=["PUT"], dependencies=[Depends(require_auth)])
router.add_api_route("/{user_id}", delete_user, methods=["DELETE"], dependencies=[Depends(require_auth)])