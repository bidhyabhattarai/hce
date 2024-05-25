from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    #address = models.CharField(max_length=100,null=True)
    #username = models.CharField(max_length=100)
   # hobby = models.TextField(default='na')    

    def str(self):
        return self.name

# Create your models here.
    

# Create your models here.

