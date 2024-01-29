from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20)

    
    def __str__ (self):
        return f"{self.first_name} {self.last_name} ({self.user_name})"





# Create your models here.

