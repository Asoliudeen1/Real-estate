from django.shortcuts import render
from realtor.models import Realtor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices

def Home(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    
    context= {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/home.html', context)


def About(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True) 
    context= {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)


