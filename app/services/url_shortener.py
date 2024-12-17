from pymongo.collection import Collection
from app.models.url_shortener import UrlShortener
from pymongo.errors import PyMongoError
from bson import json_util
import json

class UrlShortenerService():
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_shorteners(self):
        data = self.collection.find()
        url_shorteners = json.loads(json_util.dumps(list(data)))
            
        return {"ok": True, "url_shorteners": url_shorteners}
    
    def create_shortener(self, shortener: UrlShortener):
        try:
            self.collection.insert_one(shortener)
            return {"ok": True, "message": "URL Shortener created succesfully"}
        except PyMongoError as e:
            return {"ok": False, "error": e}
