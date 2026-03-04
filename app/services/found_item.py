from app.repositories import UserFoundRepository

class FoundItemService:
    def __init__(self, foundItemRepository: UserFoundRepository ):
        self.foundItemRepository = foundItemRepository
    
    def createItem(self, payload):
        item = self.foundItemRepository.create(payload)

        return item
    
    def getAllFoundItem(self, query):
        item = self.foundItemRepository
              
