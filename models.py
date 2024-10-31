from datetime import datetime
from uuid import uuid1

class User:
    @staticmethod
    def create_user(data):
        return {
            "_id": str(uuid1().hex),
            "name": data.get("name"),
            "email": data.get("email"),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

    @staticmethod
    def update_user(data):
        data["updated_at"] = datetime.utcnow()
        return data