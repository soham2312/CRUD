from src.database.mongo_client import MongoDatabaseClient
from src.models.user import User
from typing import Optional, List
import logging

class UserRepository:
    """Repository for user-related database operations."""
    def __init__(self, db_client: MongoDatabaseClient):
        self.collection = db_client.get_collection('users')

    def insert(self, user: User) -> Optional[str]:
        """Insert a new user."""
        try:
            if not user.validate():
                raise ValueError("Invalid user data")
            
            result = self.collection.insert_one(user.to_dict())
            return str(result.inserted_id)
        except Exception as e:
            logging.error(f"User insert error: {e}")
            raise

    def find_by_id(self, user_id: str) -> Optional[User]:
        """Find a user by ID."""
        try:
            user_data = self.collection.find_one({"_id": user_id})
            return User.from_dict(user_data) if user_data else None
        except Exception as e:
            logging.error(f"User find error: {e}")
            raise

    def update(self, user_id: str, update_data: dict) -> bool:
        """Update a user."""
        try:
            result = self.collection.update_one(
                {"_id": user_id},
                {"$set": update_data}
            )
            return result.modified_count > 0
        except Exception as e:
            logging.error(f"User update error: {e}")
            raise

    def delete(self, user_id: str) -> bool:
        """Delete a user."""
        try:
            result = self.collection.delete_one({"_id": user_id})
            return result.deleted_count > 0
        except Exception as e:
            logging.error(f"User delete error: {e}")
            raise

    def find_all(self) -> List[User]:
        """Retrieve all users."""
        try:
            users_data = list(self.collection.find())
            return [User.from_dict(user) for user in users_data]
        except Exception as e:
            logging.error(f"Find all users error: {e}")
            raise
        