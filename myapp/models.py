from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=255)
    point = models.IntegerField()
    
class Survivor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    infected = models.BooleanField(default=False)
    inventory = models.ManyToManyField(Resource)


