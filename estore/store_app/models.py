from django.db import models
from django.utils.text import slugify
# Create your models here.

# Categories Model
class Category(models.Model):
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

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True, blank=True)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.SET_NULL, null=True)

    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/")

    stock = models.IntegerField(default=1)
    is_featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)  # Active/Inactive Product

    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


