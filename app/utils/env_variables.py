import os
from dotenv import load_dotenv
import base64
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_DATABASE_URI="postgresql://vhhvvcrtsvmaob:7c1f68fbc4869e052ea7bbaf8059cdd1972d2a18a7a6b2c807ccc63bec773f8b@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d1kpdq7r92nktr"
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
####### Constants #######
POSTS_TABLE = 'posts'