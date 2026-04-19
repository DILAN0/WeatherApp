from models import WeatherReport

class WeatherAdapter:
    @staticmethod
    def parse_forecast(json_data):
        forecast_list = []
        # Шаг 8 означает "раз в 24 часа"
        for item in json_data['list'][::8]:
            report = WeatherReport(
                date=item['dt_txt'][:10], # Только дата (ГГГГ-ММ-ДД)
                temp=round(item['main']['temp']),
                humidity=item['main']['humidity'],
                wind_speed=item['wind']['speed'],
                desc=item['weather'][0]['description']
            )
            forecast_list.append(report)
        return forecast_list
