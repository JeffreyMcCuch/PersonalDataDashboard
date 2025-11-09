import math

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


