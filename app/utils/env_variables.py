import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:h841207s@localhost:5432/krishi'

####### Constants #######
POSTS_TABLE = 'posts'