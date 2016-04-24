from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms


# class Designer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     brand = models.CharField(max_length=100)
#     samples = models.CharField(max_length = 500)


class Designer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length = 250)
    brand = models.CharField(max_length = 500)
    sample = models.CharField(max_length = 500)
    
    # @classmethod
    # def create_designer(cls, name,email,brand,sample):
    #     designer = cls(name=name, email=email, brand=brand, sample=sample)
    #     # do something with the book
    #     return designer