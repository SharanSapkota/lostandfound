from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserLogin, UserResponse
from app.dependencies.userDependency import userServiceRepoInjected
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/login", response_model=UserResponse)
def login(payload: UserLogin, userService: UserService = Depends(userServiceRepoInjected)):
    try:
        return userService.login(payload.email, payload.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))