from django.db import models

# Create your models here.

class User(models.Model) :
    user_name = models.CharField(max_length=16)
    user_email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=256)
    user_introduction = models.TextField(max_length=600)
    user_create_date = models.DateField(auto_now=False, auto_now_add=True)
    user_point = models.IntegerField(default=0)
