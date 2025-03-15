from pymongo.collection import Collection
from app.models.url_shortener import UrlShortener
from pymongo.errors import PyMongoError
from bson import ObjectId
from datetime import datetime
from datetime import timedelta
import string
import random
from fastapi.encoders import jsonable_encoder

class UrlShortenerService():
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_shorteners(self):
        try:
            data = self.collection.find()
            url_shorteners = self._process_document(list(data))
            return {"url_shorteners": url_shorteners}
        except PyMongoError as e:
            return {"ok": False, "error": str(e)}
        
    def get_shortener(self, slug):
        try:
            data = self.collection.find_one_and_update({ "slug": slug }, { "$inc": {"clicks": 1} })
            
            if not data:
                return {"ok": False, "message": "URL Shortener not found."}
            
            return {"ok": True, "original_url": data.get('original_url')}
        except PyMongoError as e:
            return {"ok": False, "error": str(e)}
            
    
    def create_shortener(self, shortener: UrlShortener):
        try:
            slug = self._get_random_string(6)
            short_url = f"ivsm.link/{slug}"
            
            shortener["original_url"] = str(shortener["original_url"])
            
            shortener.update({
                "short_url": short_url,
                "slug": slug,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
                "clicks": 0,
                "expiration_date": datetime.now() + timedelta(days=5),
                "metadata": {
                }
            })
            
            self.collection.insert_one(shortener)
            del shortener["_id"]
            
            
            return {"ok": True, "message": "URL Shortener created succesfully", "data": jsonable_encoder(shortener)}
        except PyMongoError as e:
            return {"ok": False, "error": e}
        
    def _process_document(self, document):
        if isinstance(document, list):
            return [self._process_document(item) for item in document]
        elif isinstance(document, dict):
            return {
                key: self._process_document(value) for key, value in document.items()
            }
        elif isinstance(document, ObjectId):
            return str(document)
        elif isinstance(document, datetime):
            return document.isoformat()
        return document
    
    def _get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = "".join(random.choice(letters) for i in range(length))
        return result_str
