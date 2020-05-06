from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class CitiBike(models.Model):
    tripduration = models.IntegerField()
    starttime =  models.DateTimeField()
    stoptime = models.DateTimeField()
    start_station_id = models.IntegerField()
    start_station_name = models.TextField()
    start_station_latitude = models.FloatField()
    start_station_longitude = models.FloatField()
    end_station_id =  models.IntegerField()
    end_station_name = models.TextField()
    end_station_latitude = models.FloatField()
    end_station_longitude = models.FloatField()
    bikeid = models.IntegerField()
    usertype = models.CharField(max_length = 50)
    birth_year = models.IntegerField()
    gender = models.IntegerField()
    objects = CopyManager()
