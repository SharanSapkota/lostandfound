
from fastapi import Depends, HTTPException
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.user_service import UserService
from app.dependencies.user_dependency import get_user_service
from app.dependencies.auth_dependency import require_auth, require_admin

def register(
    payload: UserCreate,
    service: UserService = Depends(get_user_service),
):
    """Register a new user. Public."""
    try:
        return service.register(
            email=payload.email,
            firstName=payload.firstName,
            lastName=payload.lastName,
            password=payload.password,
            phone=payload.phone,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


def login(
    payload: UserLogin,
    service: UserService = Depends(get_user_service),
):
    """Login and receive a JWT token. Public."""
    try:
        token = service.login(payload.email, payload.password)
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


def get_all_users(
    _: dict = Depends(require_admin),
    service: UserService = Depends(get_user_service),
):
    """Get all users. Admin only."""
    return service.get_all()


def get_user(
    user_id: int,
    current_user: dict = Depends(require_auth),
    service: UserService = Depends(get_user_service),
):
    """Get a user by ID. Must be the same user or admin."""
    if current_user["user_id"] != user_id and current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        return service.get_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def update_user(
    user_id: int,
    payload: UserCreate,
    current_user: dict = Depends(require_auth),
    service: UserService = Depends(get_user_service),
):
    """Update a user. Must be the same user."""
    if current_user["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        return service.update(
            user_id=user_id,
            firstName=payload.firstName,
            lastName=payload.lastName,
            phone=payload.phone,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def delete_user(
    user_id: int,
    current_user: dict = Depends(require_auth),
    service: UserService = Depends(get_user_service),
):
    """Delete a user. Must be the same user or admin."""
    if current_user["user_id"] != user_id and current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        service.delete(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))