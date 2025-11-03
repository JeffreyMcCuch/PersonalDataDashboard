import math
import requests


def create_dashboard():
    
    # Display the dashboard header
    header = "Dashboard"
    print(header)
    print("".join("-" for _ in header))
    print("\nWelcome to your personal dashboard!")

    # Get and greet the user by name
    usersName = GetUserName()
    print(f"\nHello, {usersName}! Enjoy your stay on the dashboard.\n")

    #Get users fav number squared root
    GetFavNumberSquaredRoot(usersName) 

    #Get area weather
    GetAreaWaether()


def GetUserName():
    firstName = input("Please enter your First name: ")
    lastName = input("Please enter your Last name: ")
    return f"{firstName} {lastName}"

def GetAreaWaether():
    choice = input('Would you like to know the weather in your area? "yes" or "no": ').strip().lower()
    if choice == "yes":
       zipCode = checkWeatherZip()
       MakeWeatherAPICall(zipCode)
    elif choice == "no":
        print("Okay, maybe next time!")
    else:
        print("Invalid choice.")
        GetAreaWaether()

def checkWeatherZip():
    zipCode = input("Ok! Please enter your 5 digit zip code: ")
    if len(zipCode) == 5 and zipCode.isdigit():
       return zipCode
    else:
        print("Invalid zip code. Please try again.")
        checkWeatherZip()

def MakeWeatherAPICall(zipCode):
    api_key = #"your openweathermap api key here"
    country_code = "us"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode},{country_code}&appid={api_key}&units=imperial"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"Current weather in zip code {zipCode}: {temp}°F, {weather}")
    else:
        print("Error fetching weather:", data.get("message", ""))



def GetFavNumberSquaredRoot(userName):

    try:
        favoriteNumber = float(input("Please enter your favorite number: "))
        if favoriteNumber < 0:
            print("Sorry, square root of negative numbers is not supported try another number.")
            GetFavNumberSquaredRoot(userName)

        else:
            squaredRoot = math.sqrt(favoriteNumber)
            print(f"Got it {userName}! The square root of your favorite number {favoriteNumber} is {squaredRoot}\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        GetFavNumberSquaredRoot()



create_dashboard()
