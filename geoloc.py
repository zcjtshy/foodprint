import googlemaps

key='AIzaSyDvYLab-gkkGiOZHGvzFMTWUYgFmoDp3WE'    #Google Maps Geocoding API key

def coordinates(address):
    location=raw_input("Enter location")
    c=coordinates(location)
    lat=str(c[0])
    lng=str(c[1])
    coord=[]
    google_maps=googlemaps(api_key=key)
    location=google_maps.search(location=address)
    my_location=location.first()
    coord.append(my_location.lat)
    coord.append(my_location.lng)
    return coord