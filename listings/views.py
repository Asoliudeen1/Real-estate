from django.shortcuts import render

def Listings(request):
    return render(request, 'listings/listings.html')

def Listing(request, listing_id):
    return render(request, 'listings/listing.html')
