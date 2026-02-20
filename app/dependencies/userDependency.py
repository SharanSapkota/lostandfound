from app.services.user import UserService
from app.repositories.user import UserRepository

def userServiceRepoInjected():
    userRepository = UserRepository()
    return UserService(userRepository)
