import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://openweathermap.org"

    def get_data(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        return None
