from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(default="Email",max_length=100)
    password = models.CharField(default="Password",max_length=50)
    username = models.CharField(default="success",max_length=10)
    fname = models.CharField(default="200 OK",max_length=10)
    lname = models.CharField(default="200 OK",max_length=10)
    token = models.CharField(null=True,max_length=200)
    profileImage = models.CharField(default="",max_length=50)
    status = models.CharField(default="Success",max_length=10)

