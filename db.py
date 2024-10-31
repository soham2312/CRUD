from pymongo import MongoClient
from config import Config

class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.DATABASE_NAME]
        self.user = self.db.user

    def close(self):
        self.client.close()