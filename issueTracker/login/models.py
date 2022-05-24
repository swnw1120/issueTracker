from django.db import models
import random
import string

# Create your models here.
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=45)

class Session(models.Model):
    SessionKey = models.CharField(max_length=10,unique=True)
    TimeCreated = models.DateTimeField(auto_now_add=True)
    UserID = models.ForeignKey(
        User,
        on_delete= models.CASCADE
    )