from django.db import models

class Test(models.Model):
    content = models.CharField(max_length=255,default ="")
    objects = models.Manager()

class weathers(models.Model):
    wCity = models.CharField(max_length=16)
    wDate = models.CharField(max_length=16)
    wWeather = models.CharField(max_length=64)
    wTeap = models.CharField(max_length=32)
    objects = models.Manager()