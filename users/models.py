# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    def __str__(self):
        return self.email

class Profile(models.Model):
    bio = models.CharField(max_length=500, unique=True)
    avatar = models.ImageField(upload_to='avatar/')
    location = models.CharField(max_length=20, unique=True)


