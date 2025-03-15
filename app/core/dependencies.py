from fastapi import Depends
from app.db.database import MongoDB
from app.services.url_shortener import UrlShortenerService
from app.core.config import env

mongodb_credentials = env.get('mongodb')
mongodb_url = mongodb_credentials.get('url')
mongodb_port = mongodb_credentials.get('port')
mongodb_username = mongodb_credentials.get('username')
mongodb_password = mongodb_credentials.get('password')
mongodb_database = mongodb_credentials.get('database')
mongodb_collection = mongodb_credentials.get('collection')

mongodb = MongoDB(uri=f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_url}:{mongodb_port}",
                    database_name=mongodb_database)

url_shortener_collection = mongodb.get_collection(mongodb_collection)

print(f"URL Shortener ID reference: {env.get('api_key_manager').get('api_id_url_shortener')}")
print(f"URL api-key-manager: {env.get('api_key_manager').get('url')}")

def get_url_shortener_service() -> UrlShortenerService:
    return UrlShortenerService(url_shortener_collection)
