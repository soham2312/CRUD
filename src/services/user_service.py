from src.repositories.user_repository import UserRepository
from src.models.user import User
from typing import Dict, Any, Optional, List

class UserService:
    """Service layer for user-related business logic."""
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: Dict[str, Any]) -> str:
        """Create a new user."""
        user = User.from_dict(user_data)
        return self.user_repository.insert(user)

    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a user by ID."""
        user = self.user_repository.find_by_id(user_id)
        return user.to_dict() if user else None

    def update_user(self, user_id: str, update_data: Dict[str, Any]) -> bool:
        """Update an existing user."""
        return self.user_repository.update(user_id, update_data)

    def delete_user(self, user_id: str) -> bool:
        """Delete a user."""
        return self.user_repository.delete(user_id)

    def list_users(self) -> List[Dict[str, Any]]:
        """List all users."""
        users = self.user_repository.find_all()
        return [user.to_dict() for user in users]