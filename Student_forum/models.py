import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class ForumSignup(models.Model):
    username = models.EmailField(max_length=70,blank=True,unique=True)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


