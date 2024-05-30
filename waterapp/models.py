from django.db import models

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
        return self.name + self.email + self.message
