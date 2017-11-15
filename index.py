from flask import Flask, render_template, request #from --> model of something, library  of code which is Flask this time
import requests #request is like flask, library
import json
#from geoloc import coordinates
from instagram.client import InstagramAPI

app = Flask(__name__) #import  Setting up the internal of the web server, app is the variable (a flask)

@app.route("/",strict_slashes=False)
def foodprint_website():
	return render_template("index2.html")

@app.route('/top_1_restaurant', methods=["GET"])
def top_1_restaurant(image_urls=0):
	lat="51.5137947"
	lng="-0.1314185"
	access_token = '2194526392.58afe6a.1d8c1a1924104bbb8175289c1100139a'
	endpoint="http://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&access_token="+access_token
	r = requests.get(endpoint)
	data = json.loads(r.text)
	image_urls = []
	for img in data['data']:
		url = img['images']['standard_resolution']['url']
		image_urls.append(url)

	weather1 = get_weather()
	restaurants_info = search_food()
	return render_template("index3.html", image_urls=image_urls,
			weather_description=weather1, restaurants_info=restaurants_info)


	#print pic_url= data['data'][0]['images']['standard_resolution']['url']
	#image = data['data'][0]['images']['standard_resolution']['url']
	#return data['images']['standard_resolution']['url']


def get_weather():
	endpoint= "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": 'London,UK', "units":"metric", "appid":"e93fd407cde06db0608ffb006ea09c8a"}

	response = requests.get(endpoint, params=payload)
	data = response.json()

	temperature = data["main"]["temp"]
	name = data["name"]
	weather = data["weather"][0]["main"]

	if temperature <= 5:
		message = 'warm'
	else:
		message = 'to eat'
	return "It's {}C in {} today, grab something {}".format(temperature, name, message)
	
def search_food():
    resp = requests.get(
                         "https://api.foursquare.com/v2/venues/explore",
                        params = dict(
                         client_id= "ND0RYQES1ZX3UHVOYMOP2SRUEEB1IJ4DGMURFGPWBGWY0VHT",
                            client_secret= "TSBJQHVJS1FERM1K3QOYHBJKELC32N0IOQAUPDGLJ5TAINC4",
                         ll= "51.519587,-0.127012",
                        v= "20170801",
                        section= "food"))

    data = json.loads(resp.text)
    items=data['response']['groups'][0]['items']
  
    restaurants_info = []
    for item in items:
        restaurant_info = {
            'name': item['venue']['name'],
            'rating': item['venue']['rating'],
            'image': get_photos(item ['venue']['id']),
        }
        restaurants_info.append(restaurant_info)
    return restaurant_info
	

@app.route('/example_data/')
def example_data():
	location = "London"
	location_coords = coordinates(location)
	lat = str(location_coords[0])
	lng = str(location_coords[1])
	location_recent_media(lat, lng)

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	print form_data["email"]
	print requests.post(
       "https://api.mailgun.net/v3/sandbox628a63d1ccd742dd9ac51128b8c2ca53.mailgun.org/messages",
       auth=("api", "key-53a2b49ec0cae16153f7343713ebfc8d"),
       data={"from": "Excited User <mailgun@sandbox628a63d1ccd742dd9ac51128b8c2ca53.mailgun.org>",
             "to": [form_data["email"],"YOU@sandbox628a63d1ccd742dd9ac51128b8c2ca53.mailgun.org"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"}
              )
	return "Thanks for submitting!"

if __name__ == '__main__':
	app.run(debug=True)
