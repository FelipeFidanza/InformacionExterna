from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=400)
    url = models.CharField(max_length=400)

class Auctions(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=400)
    url = models.CharField(max_length=400)

class Artists(models.Model):
    title = models.CharField(max_length=250)
    about = models.TextField()
    date = models.CharField(max_length=50)
    image = models.CharField(max_length=400)
    url = models.CharField(max_length=400)