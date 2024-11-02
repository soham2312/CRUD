from flask import Flask
from src.database.mongo_client import MongoDatabaseClient
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.routes.user_routes import create_user_routes
from config.settings import config

def create_app():
    """Application factory with dependency injection."""
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize dependencies
    db_client = MongoDatabaseClient()
    user_repository = UserRepository(db_client)
    user_service = UserService(user_repository)

    # Register routes
    user_bp = create_user_routes(user_service)
    app.register_blueprint(user_bp)

    return app