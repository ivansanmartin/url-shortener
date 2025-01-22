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
    "url-shortener": {
        "reference_id": os.getenv('URL_SHORTENER_REFERENCE_ID'),
        "referece_key_id": os.getenv('URL_SHORTENER_KEY_ID'),
        "api_key": os.getenv('URL_SHORTENER_API_KEY')
    }
}