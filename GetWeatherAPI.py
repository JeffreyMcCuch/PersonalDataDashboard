import requests 

class GetWeatherAPI:
    @staticmethod
    def GetAreaWeather():
        choice = input('Would you like to know the weather in your area? ("yes" or "no"): ').strip().lower()
        if choice == "yes":
            zip_code = GetWeatherAPI.checkWeatherZip()
            GetWeatherAPI.MakeWeatherAPICall(zip_code)
        elif choice == "no":
            print("Okay, maybe next time!")
        else:
            print("Invalid choice.")
            GetWeatherAPI.GetAreaWeather()  

    @staticmethod
    def checkWeatherZip():
        zip_code = input("Ok! Please enter your 5-digit zip code: ").strip()
        if len(zip_code) == 5 and zip_code.isdigit():
            return zip_code
        else:
            print("Invalid zip code. Please try again.")
            return GetWeatherAPI.checkWeatherZip()  

    @staticmethod
    def MakeWeatherAPICall(zip_code):
        api_key = "0d093b0588c8498cfeacb9c9122dfb51" # Put  OpenWeatherMap API key here
        country_code = "us"
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}&units=imperial"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            print(f"Current weather in zip code {zip_code}: {temp}°F, {weather.capitalize()}")
        else:
            print("Error fetching weather:", data.get("message", "Unknown error"))


