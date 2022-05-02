from flask import Blueprint, request
from app.weather.controller import Weather

weather = Blueprint('weather', __name__)

@weather.get('/weather')
def get_weather_data():
    lat_lon = request.args.to_dict("lat_lon")
    return Weather.get_weather_data(lat_lon)