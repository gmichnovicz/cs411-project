import requests
import json
import pprint
from .models import Show
def get_results(artist,location):
    
    show = Show.objects.filter(artist__contains=artist.lower(), city__contains=location.lower()).first()
    if show is not None:
        results = {}
        results['name'] = show.display_artist
        results['address'] = show.location
        results['city'] = show.display_city
        results['zipcode']= show.zipcode
        results['start'] = show.start_time
        results['descript'] = show.description
    else:
        input_city = str(location)
        key = 'ZN6GPC6WGYLKI7IAZSUW' # Brooke's authentication key
        categories = 'music' 
        keywords = str(artist)

        results = {}
        response = requests.get("https://www.eventbriteapi.com/v3/events/search/?location.address="+ input_city +"&expand=organizer,venue,category&q="+keywords+"&categories=103&token=" + key)
        if (response.json()['events']==[]):
            return []
            
        results['name'] = response.json()['events'][0]['name']['text']
        results['address'] = response.json()['events'][0]['venue']['address']['address_1']
        results['city'] = response.json()['events'][0]['venue']['address']['city']
        results['zipcode'] = response.json()['events'][0]['venue']['address']['postal_code']
        results['start'] = response.json()['events'][0]['start']['local']
        results['descript'] = response.json()['events'][0]['description']['text']
        newShow = Show(artist = results['name'].lower(),city = results['city'].lower(),display_artist=results['name'],display_city=results['city'],start_time = results['start'],description=results['descript'],zipcode = results['zipcode'])
        newShow.save()
    return results



