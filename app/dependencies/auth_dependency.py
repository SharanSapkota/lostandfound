import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import SECRET_KEY, ALGORITHM
from app.constant.authError import AuthError

bearer_scheme = HTTPBearer()

def decode_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail=AuthError.TOKEN_EXPIRED)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail=AuthError.INVALID_TOKEN)


def require_auth(payload: dict = Depends(decode_token)):
    return payload


def require_admin(payload: dict = Depends(decode_token)):
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail=AuthError.FORBIDDEN)
    return payload

