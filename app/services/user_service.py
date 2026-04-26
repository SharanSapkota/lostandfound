from app.repositories.user_repository import UserRepository
from app.constant.error import AuthError
from app.models.user import User

from app.config import SECRET_KEY
import bcrypt
import jwt
from datetime import datetime, timedelta



class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, email: str, firstName: str, lastName: str, password: str, phone: str = None) -> User:
        existing = self.repo.get_by_email(email)
        if existing:
            raise ValueError("Email already registered")

        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        user = User(
            email=email,
            firstName=firstName,
            lastName=lastName,
            password_hash=hashed,
            phone=phone,
        )

        return self.repo.create(user)

    def login(self, email: str, password: str) -> str:
        user = self.repo.get_by_email(email)

        if not user:
            raise ValueError(AuthError.USER_NOT_FOUND)

        valid = bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8"))

        if not valid:
            raise ValueError(AuthError.INVALID_PASSWORD)

        payload = {
            "user_id": user.id,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "role": user.role,
            "exp": datetime.utcnow() + timedelta(hours=24)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return token

    def get_by_id(self, user_id: int) -> User:
        user = self.repo.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        return user

    def get_all(self) -> list[User]:
        return self.repo.get_all()

    def update(self, user_id: int, firstName: str = None, lastName: str = None, phone: str = None) -> User:
        user = self.repo.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        if firstName:
            user.firstName = firstName

        if lastName:
            user.lastName = lastName

        if phone:
            user.phone = phone

        return self.repo.update(user)

    def delete(self, user_id: int) -> None:
        user = self.repo.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        self.repo.delete(user)