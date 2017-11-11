from flask import Flask, render_template, request #from --> model of something, library  of code which is Flask this time
import requests #request is like flask, library
import json
from geoloc import coordinates 
from instagram.client import InstagramAPI

CONFIG = {
    'client_id': '58afe6a207db45a0a4c709a6ce8fff0a',
    'client_secret': '1d846b34d9b743b5b68d303e41eeeb57',
    'redirect_uri': 'https://food-print.herokuapp.com',
    'access_token':'2194526392.58afe6a.1d8c1a1924104bbb8175289c1100139a'}

app = Flask(__name__) #import  Setting up the internal of the web server, app is the variable (a flask)

@app.route("/") 
def hello():
	return "Hello World"

	 
@app.route("/index/<NumberOfIndex>/<hello>")  
def index(NumberOfIndex, hello):
	return int(NumberOfIndex)*hello 


@app.route("/foodprint/<name>", strict_slashes=False) 
def foodprint_website(name):
	return render_template("index.html", name=name)


@app.route("/foodprint", strict_slashes=False)
def foodprint_website2():
	return render_template("index.html")


@app.route('/location_recent_media')
def location_recent_media():
	url="http://api.instagram.com/v1/media/search?lat="+lat+"&lng="+Ing+"&distance=5000"+"&access_token="+access_token
	print url
	r=requests.get(url)
	resp=jason.loads(r.text)
	for i in range(10):
		pic_url=resp['data'][i]['images']['standard_resolution']['url']
		p=requests.get(pic_url)
		f_name=str(location)+'pic'+str(i)+'.jpg'
    	with open(f_name,'wb') as f:
    		f.write(p.content)
    		f.close()
    	print "got one"
    	Presp = JSON.Parse (resp.body)
    	print Presp.data[0].id 

location=raw_input("Enter location.\n")
c=coordinates(location)
lat=str(c[0])
lng=str(c[1])



	#access_token = request.session["2194526392.58afe6a.1d8c1a1924104bbb8175289c1100139a"]
	

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