from django.db import models

# Create your models here.


class Room(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.textField(null=True, blank=True) 
    #participants =
    updated = models.DateTimeField(auto_now=True) #Updates everytime
    created = models.DateTimeField(auto_now_add=True) #It is just once, the first time it is created


    def __str__(self):
        return self.name