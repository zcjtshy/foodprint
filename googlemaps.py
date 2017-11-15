#geocodedata
import requests

request=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=Soho,+LondonA&key=AIzaSyC-SokDY6x6E0Qj7tjyLembaj5MdOLJjYE") 

geo_location = request.json()


location = geo_location['results'][0]['geometry']['location']

longlat = geo_location['lat'], geo_location['lng']
