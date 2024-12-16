from pymongo.collection import Collection
from app.models.url_shortener import UrlShortener

class UrlShortenerService():
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_shortener(self):
        data = self.collection.find_one()
        print(data)
        return {"ok": True}
    
    def create_shortener(self, shortener: UrlShortener):
        self.collection.insert_one(shortener)
        return {"ok": True}