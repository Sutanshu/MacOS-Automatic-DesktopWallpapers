import requests
from apiKey import API_KEY
from coordinates import coordinates


def getWeather():
    content = ''
    try:
        if len(coordinates) == 2:
            result = requests.get("http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units='metric'&appid={}".format(coordinates[0], coordinates[1], API_KEY))
            content = filterWeather(result.content)
            cacheContent(content)
        else:
            print("Couldn't fetch your coordinates, would you like to enter yours? You can also enter your city name! ")
            userInput = input("Enter your city or coordinate (comma separated coordinates as: lat,lon): ")
    except:
        print("Didn't work!")
        content = getCachedContent()

    return content

def filterWeather(content): 
    pass

def getCachedContent():
    pass

def cacheContent(content):
    pass