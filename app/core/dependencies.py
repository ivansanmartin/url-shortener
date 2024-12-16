from fastapi import Depends
from app.db.database import MongoDB
from app.db.repositories.url_shortener_repository import UrlShortenerRepository
from app.services.url_shortener import UrlShortenerService
from app.core.config import env

mongodb_credentials = env.get('mongodb')
mongodb = MongoDB(uri=f"mongodb://{mongodb_credentials.get('username')}:{mongodb_credentials.get('password')}@localhost:27017",
                    database_name="url-shortener-db")

url_shortener_collection = mongodb.get_collection('url-shortener')

def get_url_shortener_repository() -> UrlShortenerRepository:
    return UrlShortenerRepository(url_shortener_collection)

def get_url_shortener_service(
    url_shortener_repository: UrlShortenerRepository = Depends(get_url_shortener_repository)
) -> UrlShortenerService:
    return UrlShortenerService(url_shortener_repository)
