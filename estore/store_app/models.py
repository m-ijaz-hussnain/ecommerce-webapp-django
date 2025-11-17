from django.db import models

# Create your models here.

# Categories Model
class Categorie(models.Model):
    name = models.CharField(max_length = 200)


# Brands Model
class Brand(models.Model):
    name = models.CharField(max_length = 200)


# Color Model
class Color(models.Model):
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length = 60)


# Filter_Price Model
class Filter_Price(models.Model):
    
    FILTER_PRICE = (
        ('0 TO 20','0 TO 20'),
        ('20 TO 50','20 TO 50'),
        ('50 TO 100','50 TO 100'),
        ('100 TO 500','100 TO 500'),
        ('500 TO 1000','500 TO 1000'),
        ('1000 TO 2000','1000 TO 2000'),
        ('2000 TO 3000','2000 TO 3000'),
        ('3000 TO 4000','3000 TO 4000'),
        ('4000 TO 5000','4000 TO 5000'),
    )

    price = models.CharField(choices=FILTER_PRICE, max_length = 60)
