from django.db import models
from datetime import datetime
from realtor.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqrf = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/')
    photo1 = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/', blank=True)
    photo5 = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/', blank=True)
    photo6 = models.ImageField(default='default.jpg', upload_to='photo/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title