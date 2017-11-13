from flask import Flask, render_template, request #from --> model of something, library  of code which is Flask this time
import requests #request is like flask, library
import json
from geoloc import coordinates 
from instagram.client import InstagramAPI

app = Flask(__name__) #import  Setting up the internal of the web server, app is the variable (a flask)

@app.route("/",strict_slashes=False) 
def foodprint_website():
	return render_template("index.html")
	 
@app.route("/index/<NumberOfIndex>/<hello>")  
def index(NumberOfIndex, hello):
	return int(NumberOfIndex)*hello 

@app.route('/location_recent_media/<lat>/<lng>')
def location_recent_media(lat,lng):
	access_token = '2194526392.58afe6a.1d8c1a1924104bbb8175289c1100139a'
	url="http://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&access_token="+access_token
	print url
	response = requests.get(url)
	data = json.loads(response.text)
	data['images']['standard_resolution']['url']
		

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
