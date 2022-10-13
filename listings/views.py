from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .choices import price_choices, bedroom_choices, state_choices 

def Listings(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_listings = paginator.get_page(page_number)

    context= {
        'listings':page_listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listingObj = get_object_or_404(Listing, id=listing_id)
    context= {
        'listingObj':listingObj,
    }
    return render(request, 'listings/listing.html', context)



def Search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # KEWORDS
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
     # STATE
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
     # BEDROOM
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    

    

    context= {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
