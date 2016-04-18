from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=250)
	
	

	def __unicode__(self):
		return self.user.email
