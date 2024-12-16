from fastapi import Depends
from app.db.database import MongoDB
from app.services.url_shortener import UrlShortenerService
from app.core.config import env

mongodb_credentials = env.get('mongodb')
mongodb_url = mongodb_credentials.get('url')
mongodb_port = mongodb_credentials.get('port')
mongodb_username = mongodb_credentials.get('username')
mongodb_password = mongodb_credentials.get('password')

mongodb = MongoDB(uri=f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_url}:{mongodb_port}",
                    database_name="url-shortener-db")

url_shortener_collection = mongodb.get_collection('url-shortener')

def get_url_shortener_service() -> UrlShortenerService:
    return UrlShortenerService(url_shortener_collection)
