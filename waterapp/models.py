from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
# class emp(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField(default=20)
    
#     def __str__(self):
#         return f'{self.name}, {self.age}'
    

class emp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null = True, blank=True)
    message = models.TextField(null= True, blank=True)

    def __str__(self):
        return f'{self.name} , {self.email} , {self.message}'
    
class signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(null = True, blank=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username} , {self.email} , {self.password} , {self.confirm_password}'
    
class login (models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.username} , {self.password}'