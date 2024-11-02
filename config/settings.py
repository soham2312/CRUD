import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "flask_mongo_crud")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))

config = Settings()