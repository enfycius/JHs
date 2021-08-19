from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=30, blank = True, null = True)
    password = models.CharField("Password", max_length=20, blank = True, null = True)