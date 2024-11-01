import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "flask_mongo_crud")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")