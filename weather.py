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
   if temperature <=5;
       message = 'warm'
   else:
       message= 'to eat'         
    
print u"It's {}C in {} today, grab something "weathercomm" .format(temperature, name)