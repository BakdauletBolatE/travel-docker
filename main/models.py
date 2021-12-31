from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=255,default='Kazakhstan')

class TravelCity(models.Model):

    name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='City/')
    price = models.IntegerField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)


class TravelEvent(models.Model):

    travelCity = models.ForeignKey(TravelCity,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Gallery(models.Model):

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Gallery/')

class UserEvent(models.Model):
    event = models.ForeignKey(TravelEvent,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
