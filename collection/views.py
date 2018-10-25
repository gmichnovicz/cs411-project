from django.shortcuts import render
from collection.forms import QueryForm
from django.shortcuts import redirect
from django.template.loader import get_template
from collection import services

# Create your views here.
def index(request): 
    # this is your new view
    return render(request, 'index.html')

def apiquery(request):
    form_class = QueryForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        artist = request.POST.get('artist', '')
        location = request.POST.get('location', '')
        results = services.get_results(artist,location)
        # if results == []: ADD ERROR CATCHING
        #     pass
        return render(request,'results.html',{
            'artist': results['name'],
            'address':results['address'],
            'city':results['city'],
            'zip':results['zipcode'],
            'start':results['start'],
            'descript':results['descript']
        })

    return render(request, 'apiquery.html', {
        'form': form_class,
    })
