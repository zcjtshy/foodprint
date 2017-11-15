

#geocodedata
request=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=Soho,+LondonA&key=AIzaSyC-SokDY6x6E0Qj7tjyLembaj5MdOLJjYE") 

geodata= request.json()

print geodata[]

#notsure how to get coordinates only, not sure if craigs code works


#geo map code into flask
from flask import flask
from flask.ext.googlemaps import Googlemaps
app = Flask(foodprint)
Googlemaps(app)


#adding london weather

endpoint= "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": London,UK, "units":"metric", "appid":"e93fd407cde06db0608ffb006ea09c8a"}

response = requests.get(endpoint, params=payload)

print response.url
print response.status_code
print response.headers["content-type"]

data = response.json()

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]

weathercomm=
    "warm" if "temperature"<= 5
    "to eat" elif "temperature"> 5
#can someone check this we could have a weather point     
    
print u"It's {}C in {} today, grab something "weathercomm" .format(temperature, name)

