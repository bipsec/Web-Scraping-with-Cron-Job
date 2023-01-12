from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class AirbnbData(models.Model):

        Categories = models.TextField(blank=True)
        Price =  models.FloatField(blank=True)
        Reviews =  models.TextField(blank=True)
        Rating =  models.FloatField(blank=True)
        # Hosted_By =  models.TextField(blank=True)
        Description =  models.TextField(blank=True)
        URL = models.URLField(primary_key=True)
        Amenities =  models.TextField(blank=True)
        # HouseRule =  models.TextField(blank=True)
        Location =  models.TextField(blank=True)
        SafetyProperty =  models.TextField(blank=True)
        Image =  models.CharField(max_length=200, blank=True)


        

        class Meta:
                db_table = "airbnbData"

        


  



        

