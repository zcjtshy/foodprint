import requests,json


def search_food():
    return requests.get(
                         "https://api.foursquare.com/v2/venues/explore",
                        params = dict(
                         client_id= "ND0RYQES1ZX3UHVOYMOP2SRUEEB1IJ4DGMURFGPWBGWY0VHT",
                            client_secret= "TSBJQHVJS1FERM1K3QOYHBJKELC32N0IOQAUPDGLJ5TAINC4",
                         ll= "51.519587,-0.127012",
                        v= "20170801",
                        section= "food"))

#print search_food().json()
resp=search_food()
data = json.loads(resp.text)


items=data['response']['groups'][0]['items']

for item in items:
    print item['venue']['name'] + ' Rating: ' + str(item['venue']['rating'])
venue_id=data['response']['groups'][0]['items'][0]['venue'] ['id']

#venue = data['response']['groups'][0]['items'][0]['venue']
#print venue['name']
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
#resp1=get_photos(venue['id'])
size="500x300"
#data = json.loads(resp1.text)
#photo = data['response']['photos']['items'][0]['prefix']+size+data['response']['photos']['items'][0]['suffix']
#print photo
