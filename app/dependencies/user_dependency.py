from lostAndFound.app.services.user_service import UserService
from lostAndFound.app.repositories.user_repository import UserRepository

def userServiceRepoInjected():
    userRepository = UserRepository()
    return UserService(userRepository)
