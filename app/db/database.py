from app.core.config import env
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

mongo_envs = env.get('mongodb')

def get_database():
    try:
        username = mongo_envs.get('username')
        password = mongo_envs.get('password')
        CONNECTION_STRING = f"mongodb://{username}:{password}@localhost:27017/url-shortener-db?authSource=admin"
        
        client = MongoClient(CONNECTION_STRING)
        client.admin.command('ping')
        
        return client['url-shortener-db']
    
    except ConnectionFailure as e:
        print(f"No se pudo conectar a MongoDB: {e}")
        return None


