from unicodedata import name
from django.db import models


# Create your models here.
class category (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

class product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=6,decimal_places=3)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name