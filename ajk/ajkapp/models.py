from django.db import models

# Create your models here.






class beijin(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=32)
    average_price = models.IntegerField()
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    count = models.IntegerField()


class guangzhou(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=32)
    average_price = models.IntegerField()
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    count = models.IntegerField()

class shenzhen(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=32)
    average_price = models.IntegerField()
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    count = models.IntegerField()

class shanghai(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=32)
    average_price = models.IntegerField()
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    count = models.IntegerField()


class taiyuan(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.CharField(max_length=32)
    average_price = models.IntegerField()
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    count = models.IntegerField()



class average_prices(models.Model):
    id = models.BigAutoField(primary_key=True)
    City = models.CharField(max_length=32)
    Average_Price = models.IntegerField()
