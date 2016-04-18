from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from signups.models import CustomerUser

class SignUpForm(ModelForm):
	# name = forms.CharField(label='name')
	# email = forms.EmailField(label='email address')

	class Meta:
		# model = CustomerUser
		fields = ['name','email']

	def save(self):
		data = self.cleaned_data

		_name = data['name']
		_email = data['email']
		_username = _email
		user = User.objects.create_user(username=_name, email=_email)
		user.save()
