from app.posts.models import PostGresDb
from app.utils.response_utils import throw_error, throw_response

pg = PostGresDb()
class PostsController():
    def push_posts_to_db(post_data):
        if not post_data:
            throw_error(status = 422,message = "No payload found")

        message = post_data.get('message')
        lat = post_data.get('lat')
        lon = post_data.get('lon')
        pg.create_table()
        
        return pg.insert_one(message, lat, lon)
    
    def get_posts(lat, lon, page):
        recent_nearby_posts = pg.get_data_per_page(lat, lon, page, per_page=10)
        return throw_response(recent_nearby_posts)
        