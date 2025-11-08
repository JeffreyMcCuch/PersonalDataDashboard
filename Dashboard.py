import math
from GetWeatherAPI import GetWeatherAPI  # ✅ Import should be near the top

@ staticmethod
def GetUserName(firstName, lastName):
    return f"{firstName} {lastName}"


@ staticmethod
def GetFavNumberSquaredRoot(favoriteNumber):
        if favoriteNumber < 0:
            return False
        else:
            squaredRoot = math.sqrt(favoriteNumber)
            return squaredRoot        


