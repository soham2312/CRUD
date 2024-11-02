from flask import Blueprint, request, jsonify
from src.services.user_service import UserService
from src.database.mongo_client import MongoDatabaseClient
from src.repositories.user_repository import UserRepository

def create_user_routes(user_service: UserService):
    """Create user routes with dependency injection."""
    user_bp = Blueprint('user', __name__)

    @user_bp.route('/user', methods=['POST'])
    def create_user():
        try:
            user_data = request.get_json()
            user_id = user_service.create_user(user_data)
            return jsonify({"id": user_id}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Internal server error"}), 500

    @user_bp.route('/user/<user_id>', methods=['GET'])
    def get_user(user_id):
        user = user_service.get_user(user_id)
        return (jsonify(user), 200) if user else (jsonify({"error": "User not found"}), 404)

    @user_bp.route('/user/<user_id>', methods=['PUT'])
    def update_user(user_id):
        try:
            update_data = request.get_json()
            success = user_service.update_user(user_id, update_data)
            return (jsonify({"message": "Updated"}), 200) if success else (jsonify({"error": "User not found"}), 404)
        except Exception as e:
            return jsonify({"error": "Internal server error"}), 500

    @user_bp.route('/user/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        success = user_service.delete_user(user_id)
        return (jsonify({"message": "Deleted"}), 200) if success else (jsonify({"error": "User not found"}), 404)

    @user_bp.route('/users', methods=['GET'])
    def list_users():
        users = user_service.list_users()
        return jsonify(users), 200

    return user_bp