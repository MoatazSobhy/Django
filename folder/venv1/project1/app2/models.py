from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    choose = [
        ('Smart Devices','Smart Devices'),
        ('Cars','Cars'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=choose)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Product"
        ordering = ['name']
    
class Date(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    def __str__(self):
        return self.item_name
    
class User(models.Model):
    user_name = models.CharField(max_length=50)
    key = models.ForeignKey(Item, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.user_name
    
    



    
    
    
    