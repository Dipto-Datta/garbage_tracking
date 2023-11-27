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

    

