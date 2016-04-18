from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django import forms

# Create your models here.
# class Address(models.Model):
#     address_1 = models.CharField(verbose_name="address", max_length=250)
#     address_2 = models.CharField(verbose_name="address cont'd", max_length=250)
#     city = models.CharField(max_length=100)
#     zip_code = models.CharField(verbose_name="ZIP code", max_length=10)
#     country = models.CharField(max_length=50) # TODO: Update to django-countries
    
# class BaseUser(AbstractUser):
#     # all common fields go here
# 	name = models.CharField(max_length=250)
# 	address = models.ManyToManyField(Address)

# # 	def __unicode__(self):
# # 		return django.contrib.auth.models.AbstractUser.email

# class StoreOwnerUser(BaseUser):
#     # All Store Owner specific attribute goes here
#     desc = models.CharField(max_length=500)

#     class Meta:
#         verbose_name = 'Store Owner'


# class Designs(models.Model):
#     designer = models.ForeignKey(StoreOwnerUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250, primary_key=True) # Name of design
#     image = models.ImageField() # Image for the design
#     desc = models.CharField(max_length=500) # description of the design
#     free_size = models.BooleanField() # Is the design free size, or does it require measurements
#     sml_measurement = models.BooleanField() # Does the design accept S,M,L,XL measurements, or does it require bespoke measurements

# class CustomerUser(BaseUser):
#     # All Customer specific attribute goes here
#     customer_id = models.CharField(max_length=30, unique=True)
#     SIZES = (
#         ('XS','X-SMALL'),
#         ('S','SMALL'),
#         ('M','MEDIUM'),
#         ('L','LARGE'),
#         ('XL','X-LARGE'),
#         )
#     SML_size = models.CharField(max_length=2, choices=SIZES)
#     #TODO: Implement measurements model

#     class Meta:
#         verbose_name = 'Customer'
        

