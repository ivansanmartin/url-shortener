from dotenv import load_dotenv
import os

load_dotenv()

env = {
    "mongodb": {
        "username": os.getenv('MONGODB_USERNAME'),
        "password": os.getenv('MONGODB_PASSWORD')    
    }
}