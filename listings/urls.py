from django.urls import path
from . import views

urlpatterns = [
    path('', views.Listings, name='listings'),
    path('<int:listing_id>', views.Listing, name='listing'),
]