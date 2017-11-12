import googlemaps

key='AIzaSyDvYLab-gkkGiOZHGvzFMTWUYgFmoDp3WE'    #Google Maps Geocoding API key

def coordinates(address):
    google_maps = googlemaps.client(key=key)
    location = google_maps.geocode(address)
    geo_location = location[0]['geometry']['location']
    return geo_location['lat'],geo_location['ing']