from django.db import models
from django.contrib.auth.models import User

class Broker(models.Model):
    br = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=70,blank=True)
    
    def __str__(self):
        return self.name

class Adv(models.Model):
    broker=models.ForeignKey('broker.Broker',on_delete=models.CASCADE,related_name='advs')
    title=models.CharField(max_length=500)
    bath=models.IntegerField()
    balcony=models.IntegerField()
    bedrooms=models.IntegerField()
    area_sqft=models.FloatField()
    area_type=models.CharField(max_length=100)
    hk=models.IntegerField()
    location=models.CharField(max_length=500)

    def __str__(self):
        return self.title
