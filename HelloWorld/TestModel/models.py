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

class phone(models.Model):
    wMark = models.CharField(max_length=256)
    wNote = models.CharField(max_length=1024)
    wPrice = models.CharField(max_length=32)
    wSrc1 = models.CharField(max_length=256,default ="")
    wSrc2 = models.CharField(max_length=256,default ="")
    objects = models.Manager()

class movie(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

