from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(default="Email",max_length=100)
    username = models.CharField(default="USERNAME",unique=True,max_length=50)
    fname = models.CharField(default="First Name",max_length=50)
    lname = models.CharField(default="Last Name",max_length=50)
    password = models.CharField(default="Password",max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    

