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

@app.route('/location_recent_media', methods=["GET"])
def location_recent_media():
	lat="51.507114863624"
	lng="-0.12731805236353"
	access_token = '2194526392.58afe6a.1d8c1a1924104bbb8175289c1100139a'
	endpoint="http://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&access_token="+access_token
	r = requests.get(endpoint)
	data = json.loads(r.text)
	image_urls = []
	for img in data['data']:
		url = img['images']['standard_resolution']['url']
		image_urls.append(url)
	return ','.join(image_urls) 

	#print pic_url= data['data'][0]['images']['standard_resolution']['url']
		

	#image = data['data'][0]['images']['standard_resolution']['url']
	#return data['images']['standard_resolution']['url']
				
	#print data
	#return ['data']['meta']['code']
	#data['images']['standard_resolution']['url']
	 		
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
