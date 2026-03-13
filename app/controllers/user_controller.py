from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from lostAndFound.app.schemas.user_schema import UserLogin, UserResponse
from lostAndFound.app.dependencies.user_dependency import userServiceRepoInjected
from lostAndFound.app.services.user_service import UserService

def login(payload: UserLogin, userService: UserService = Depends(userServiceRepoInjected)):
    try:
        return userService.login(payload.email, payload.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))