from django.db import models

# Create your models here.


class SiteUser(models.Model):
    fname= models.CharField(max_length=64)
    lname= models.CharField(max_length=64)
    address= models.CharField(max_length=256)
    email= models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=11)
    favorite_movie = models.CharField(max_length=128)
    


