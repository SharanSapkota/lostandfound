from app.repositories.user import UserRepository
from app.config import AuthError
import os 

SECRET_TOKEN = SECRET_TOKEN = os.environ.get("SECRET_TOKEN")

class UserService:
    def __init__(self, userRepository: UserRepository):
            self.userRepository = userRepository

    def login(self, email: string, password: string):
        user = self.userRepository.get_by_email(email)

        if not user:
            raise ValueError(AuthError.USER_NOT_FOUND)
        
        checkPassword = bcrypt.checkpw(password.encode('utf-8'), user.has_password.encode('utf-8'))
        if not checkPassword:
            raise ValueError(AuthError.INVALID_PASSWORD)

        payload = {
            "user_id": user.id,
            "firstName": user.firstName,
            "lastName": user.lastName
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return token