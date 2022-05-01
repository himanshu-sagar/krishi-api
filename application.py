from flask import Flask
import toml
from app.posts.routs import posts
#from app.posts.models import db
from flask_cors import CORS

def initialize_app(testing: bool = False):
    app = Flask(__name__)
    CORS(app, resources = {r"/*": {"origins": "*"}})

    #db.init_app(app)
    # Register Blueprints here
    app.register_blueprint(posts)


    @app.route('/', methods = ["GET"])
    def index():
        data = toml.load("pyproject.toml")
        return f"<h1>Krishi App APIs</h1> <h2>Version : {data['tool']['poetry']['version']}</h2>"
    return app