from dotenv import load_dotenv
import os

load_dotenv()

env = {
    "mongodb": {
        "url": os.getenv('MONGODB_URL'),
        "port": os.getenv('MONGODB_PORT'),
        "username": os.getenv('MONGODB_USERNAME'),
        "password": os.getenv('MONGODB_PASSWORD'),    
        "database": os.getenv('MONGODB_DATABASE'),    
        "collection": os.getenv('MONGODB_COLLECTION'),   
    },
    "api_key_manager": {
        "url": os.getenv('URL_API_KEY_MANAGER'),
        "api_id_url_shortener": os.getenv('API_ID_URL_SHORTENER')
    }
}