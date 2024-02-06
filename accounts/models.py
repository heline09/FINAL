from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username




# Create your models here.

