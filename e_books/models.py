from enum import unique
from django.db import models

# Create your models here.

#user Rgistration model
class Userregistration(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username



# book model
class Book(models.Model):
    user = models.ForeignKey(Userregistration, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


