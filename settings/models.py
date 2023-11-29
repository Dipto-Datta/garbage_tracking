from django.db import models

# Create your models here.


class Recycling_Center(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    phone = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class GarbageType(models.Model):
    name = models.CharField(max_length=100,unique=True) 
    unit = models.IntegerField(default=1)
    per_unit_price = models.IntegerField(default=20)
    total_price = models.IntegerField(default=0,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Calculate total_price based on unit and per_unit_price
        self.total_price = self.unit * self.per_unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    

