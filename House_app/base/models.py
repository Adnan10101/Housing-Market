from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.EmailField(unique = True,primary_key=True)
    phone_no = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add = True)