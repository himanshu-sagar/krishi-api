from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils.response_utils import throw_error
from app.utils.env_variables import SQLALCHEMY_DATABASE_URI, POSTS_TABLE
from app.utils.common import validate_and_format_coordinates
from app.utils.common import seconds_to_text
#db = SQLAlchemy()

class PostGresDb:
    # TODO: Create Destructor for closing session
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def execute_query(self, query):
        res = self.session.execute(query)
        self.session.commit()
        return res

    def create_table(self):
        #try:
        query = f"CREATE TABLE IF NOT EXISTS {POSTS_TABLE} (id serial PRIMARY KEY, Message text, Posted_At TIMESTAMP, Location point);"
        self.execute_query(query)
        #except Exception as e:
            #return throw_error(message = str(e))
        return "Success"

    def insert_one(self, message, lat, lon):
        try:
            # validate if coordinates are correct
            lat, lon = validate_and_format_coordinates(lat, lon)
            if lat == None or lon == None:
                return throw_error(message = "Invalid Coordinates", error= "Validation Error", status=422)
            location = str((lon, lat))
            query = f"INSERT INTO {POSTS_TABLE} (Message, Posted_At, Location) VALUES ('{message}', CURRENT_TIMESTAMP, '{location}')"
            self.execute_query(query)
            self.session.commit()
        except Exception as e:
            return throw_error(message = str(e))
        
        return "Your Post Inserted SuccessFully"

    def get_data_per_page(self, lat, lon, page, per_page):
        if page < 1:
            return []
        current_coordinate = f'{lon}, {lat}'
        query = f"select id as Serial_Num, Message, ('{current_coordinate}' <-> Location) as Distance, Posted_At from {POSTS_TABLE} order by Posted_At DESC, distance ASC OFFSET {per_page*(page-1)} LIMIT {per_page};"
        rows = self.session.execute(query)
        posts_data = []
        for row in rows:
            temp_dict = {}
            temp_dict['Serial_Num'] = row[0]
            temp_dict['Message'] = row[1]
            temp_dict['Distance'] = row[2]
            temp_dict['Posted_At'] = row[3]
            tf = datetime.utcnow()-row[3]
            print(tf.total_seconds())
            temp_dict['Time_Stamp'] = seconds_to_text(tf.total_seconds())
            posts_data.append(temp_dict)
        return posts_data
