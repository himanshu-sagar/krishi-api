import os
from dotenv import load_dotenv
import base64
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_POSTGRES')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
####### Constants #######
POSTS_TABLE = 'posts'