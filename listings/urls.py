from django.urls import path
from . import views

urlpatterns = [
    path('', views.Listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search/', views.Search, name='search'),
]