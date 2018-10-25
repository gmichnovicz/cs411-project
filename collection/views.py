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
        a, l = services.get_results(artist,location)
        return render(request,'results.html',{
            'artist': a,
            'location':l,
        })

    return render(request, 'apiquery.html', {
        'form': form_class,
    })
