from django.db import models

# Create your models here.
class parkinson(models.Model):
   login = models.CharField(max_length=70, blank=False, default='')
   password = models.CharField(max_length=200,blank=False, default='')
   stepsNum =  models.IntegerField() 