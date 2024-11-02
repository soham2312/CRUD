from pymongo import MongoClient
from config.settings import config
import time
import logging

class MongoDatabaseClient:
    """Robust MongoDB client with connection retry mechanism."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize MongoDB connection with retry logic."""
        self.client = None
        self.db = None
        self._connect_with_retry()

    def _connect_with_retry(self, max_retries=5):
        """Establish MongoDB connection with exponential backoff."""
        for attempt in range(1, max_retries + 1):
            try:
                self.client = MongoClient(config.MONGO_URI)
                self.db = self.client[config.DATABASE_NAME]
                
                # Verify connection
                self.client.admin.command('ismaster')
                logging.info("Successfully connected to MongoDB")
                return
            
            except Exception as e:
                wait_time = 2 ** attempt  # Exponential backoff
                logging.warning(f"MongoDB connection attempt {attempt} failed: {e}")
                
                if attempt == max_retries:
                    logging.error("Could not establish MongoDB connection")
                    raise ConnectionError("Failed to connect to MongoDB")
                
                time.sleep(wait_time)

    def get_collection(self, collection_name):
        """Get a specific MongoDB collection."""
        return self.db[collection_name]

    def close(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            logging.info("MongoDB connection closed")