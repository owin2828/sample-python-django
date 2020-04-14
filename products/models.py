from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    discount = models.FloatField()