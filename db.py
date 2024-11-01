from pymongo import MongoClient
from config import Config
import time

class Database:
    def __init__(self):
        self._connect_with_retry()
        self.db = self.client[Config.DATABASE_NAME]
        self.user = self.db.user

    def _connect_with_retry(self, max_retries=5):
        retries = 0
        while retries < max_retries:
            try:
                self.client = MongoClient(Config.MONGO_URI)
                self.client.admin.command('ismaster')
                print("Successfully connected to MongoDB")
                return
            except Exception as e:
                retries += 1
                print(f"Failed to connect to MongoDB (attempt {retries}/{max_retries}): {str(e)}")
                if retries < max_retries:
                    time.sleep(2)
        raise Exception("Could not connect to MongoDB")

    def close(self):
        self.client.close()