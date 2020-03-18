from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name


class NutritionValue(models.Model):
    calories = models.DecimalField(max_digits=5, decimal_places=0)
    fat = models.CharField(max_length=10, default='')
    saturates = models.CharField(max_length=10, default='')
    carbs = models.CharField(max_length=10, default='')
    sugars = models.CharField(max_length=10, default='')
    polyols = models.CharField(max_length=10, default='')
    fibre = models.CharField(max_length=10, default='')
    protein = models.CharField(max_length=10, default='')
    salt = models.CharField(max_length=10, default='')
    
    def __str__(self):
        return self.name