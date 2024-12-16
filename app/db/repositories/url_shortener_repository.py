from pymongo.collection import Collection

class UrlShortenerRepository:
    def __init__(self, collection: Collection):
        self.collection = collection
    
    def create_shortener(self):
        pass
    
    def get_shorteners(self):
        shorteners = list(self.collection.find())
        for shortener in shorteners:
            shortener["_id"] = str(shortener["_id"])
        return shorteners
        
    
    def update_shortener(self):
        pass
    
    def delete_shortener():
        pass