from flask import Flask
import toml
from app.posts.routs import posts
from app.weather.routs import weather

from flask_cors import CORS

# Initialize Flask App
def initialize_app(testing: bool = False):
    app = Flask(__name__)
    CORS(app, resources = {r"/*": {"origins": "*"}})

    # Register Blueprints here
    app.register_blueprint(posts)
    app.register_blueprint(weather)

    @app.route('/', methods = ["GET"])
    def index():
        data = toml.load("pyproject.toml")
        return f"<h1>Krishi App APIs</h1> <h2>Version : {data['tool']['poetry']['version']}</h2>"
    return app