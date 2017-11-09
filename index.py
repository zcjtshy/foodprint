from flask import Flask, render_template, request #from --> model of something, library  of code which is Flask this time
import requests #request is like flask, library

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