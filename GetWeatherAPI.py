import requests

class GetWeatherAPI:
    @staticmethod
    def MakeWeatherAPICall(zip_code):
        api_key = "API KEY HERE"  # OpenWeatherMap API key
        country_code = "us"
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}&units=imperial"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            localweather = f"Current weather in zip code {zip_code}: \n{temp}°F {weather.capitalize()}"
            return localweather
        else:
            return False
