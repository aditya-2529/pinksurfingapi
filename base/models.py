from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    profile_image = models.URLField(default="",max_length=150)
    fcm_token = models.CharField(max_length=255, null=True)

