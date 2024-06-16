from django.db import models

# Create your models here.

class Login(models.Model):
    email = models.CharField(default="Email",max_length=100)
    password = models.CharField(default="Password",max_length=50)
    isLoggedIn = models.BooleanField()

    

