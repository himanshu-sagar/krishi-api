import requests
from app.utils.env_variables import WEATHER_API_KEY
from app.utils.response_utils import throw_response, throw_error

class Weather:
    def get_weather_data_helper(lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}'
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    def get_weather_data(lat_lon):
        try:
            weather_data = Weather.get_weather_data_helper(lat_lon["lat"], lat_lon["lon"])
        except Exception as e:
            return throw_error(e)
        return throw_response(weather_data)