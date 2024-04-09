from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    Location=models.CharField(max_length=100, null=True, blank=True)
    phone_number=models.CharField(max_length=13, null=True, blank=True)
    hobby=models.CharField(max_length=50, null=True, blank=True)
