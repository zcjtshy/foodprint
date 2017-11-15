import requests,json


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
    

<<<<<<< HEAD
#venue = data['response']['groups'][0]['items'][0]['venue']
#print venue['name'
=======
venue = data['response']['groups'][0]['items'][0]['venue']
#print venue['name']
>>>>>>> e0e721cfa7272b8395c7cd99e2cc11f5b93bef99
#print venue['location']
#[0].items[0].venue.name
#for key, value in data['response'].iteritems() :
#print key



def get_photos(venue_id):
    return requests.get(
                        "https://api.foursquare.com/v2/venues/"+venue_id+"/photos",
                        params = dict(
                                      client_id= "ND0RYQES1ZX3UHVOYMOP2SRUEEB1IJ4DGMURFGPWBGWY0VHT",
                                      client_secret= "TSBJQHVJS1FERM1K3QOYHBJKELC32N0IOQAUPDGLJ5TAINC4",
                                      v= "20170801"))
resp1=get_photos(venue['id'])
size="500x300"
data = json.loads(resp1.text)
photo = data['response']['photos']['items'][20]['prefix']+size+data['response']['photos']['items'][20]['suffix']
print photo
