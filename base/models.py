from django.db import models

# Create your models here.

class Login(models.Model):
    email = models.CharField(default="Email",max_length=100)
    password = models.CharField(default="Password",max_length=50)
    status = models.CharField(default="success",max_length=10)
    message = models.CharField(default="200 OK")
    isLoggedIn = models.BooleanField()

class Register(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    entered_otp = models.CharField(max_length=6)
    status = models.CharField(default="success",max_length=10)
