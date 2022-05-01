from flask import Blueprint, request
from app.posts.controller import PostsController

posts = Blueprint('posts', __name__)

@posts.post('/create_post')
def create_post():
    post_data = request.get_json(force = True)
    return PostsController.push_posts_to_db(post_data)

@posts.get('/get_posts/<page>')
def get_posts(page):
    post_data = request.args.to_dict("post_data")
    page= int(page)
    return PostsController.get_posts(float(post_data.get('lat')), float(post_data.get('lon')), page)