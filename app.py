from flask import Flask
from routes.user_routes import user
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(user)
    
    return app

if __name__ == "__main__":
    app = create_app()
    # Updated host to allow external connections
    app.run(host='0.0.0.0', port=5000, debug=True)