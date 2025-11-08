import math
from GetWeatherAPI import GetWeatherAPI  # ✅ Import should be near the top

def create_dashboard():
    # Display the dashboard header
    header = "Dashboard"
    print(header)
    print("".join("-" for _ in header))
    print("\nWelcome to your personal dashboard!")

    # Get and greet the user by name
    usersName = GetUserName()
    print(f"\nHello, {usersName}! Enjoy your stay on the dashboard.\n")

    # Get user's favorite number and display its square root
    GetFavNumberSquaredRoot(usersName)

    # Get area weather using  imported class
    GetWeatherAPI.GetAreaWeather()  

def GetUserName():
    firstName = input("Please enter your first name: ").strip()
    lastName = input("Please enter your last name: ").strip()
    return f"{firstName} {lastName}"

def GetFavNumberSquaredRoot(userName):
    try:
        favoriteNumber = float(input("Please enter your favorite number: "))
        if favoriteNumber < 0:
            print("Sorry, square root of negative numbers is not supported. Try another number.")
            GetFavNumberSquaredRoot(userName) 
        else:
            squaredRoot = math.sqrt(favoriteNumber)
            print(f"Got it, {userName}! The square root of your favorite number {favoriteNumber} is {squaredRoot}\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        GetFavNumberSquaredRoot(userName) 
        
create_dashboard() 

