from app.services import FoundItemService
from app.repositories import FoundItemRepository

def FoundServiceServiceRepoInjected():
    foundItemRepository = FoundItemRepository()
    return FoundItemService(foundItemRepository)
