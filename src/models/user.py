from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4
from typing import Optional, Dict, Any

@dataclass
class User:
    """Immutable user model with validation."""
    id: str = field(default_factory=lambda: str(uuid4()))
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Create a User instance from a dictionary."""
        return cls(
            id=data.get('id', str(uuid4())),
            name=data.get('name'),
            email=data.get('email')
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert User to a dictionary for database storage."""
        return {
            "_id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": datetime.utcnow()
        }

    def validate(self) -> bool:
        """Basic validation for user data."""
        return all([
            self.name and len(self.name) > 2,
            self.email and '@' in self.email
        ])