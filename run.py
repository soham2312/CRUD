from src.app import create_app
from config.settings import config

if __name__ == "__main__":
    app = create_app()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)