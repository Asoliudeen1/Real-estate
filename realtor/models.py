from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', default='default.jpg')
    description = models.TextField(max_length=200, blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
