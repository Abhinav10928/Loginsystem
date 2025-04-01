from django.db import models

# Create your models here.
#Model created
class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=10)
    Password = models.CharField(max_length=8)