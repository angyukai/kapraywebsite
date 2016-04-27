from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.template import loader
from forms import SignUpForm
from models import Designer

from django.core.mail import send_mail
# from models import CustomerUser

# Create your views here.

def home(request):
    
    return render(request, 'signups/signups.html')
    
def signup(request):
	
    
	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		brand = request.POST['brand']
		sample = request.POST['sample']
		
 		designer = Designer.create(name=name, email=email, brand = brand, sample = sample)
		designer.save()
		send_mail(
			'New User', 
			'New Designer signed up. \nName:'+designer.name+'\nEmail:'+designer.email+'\nSample:'+designer.s+, 
			'noreply@justkapray.online',
    		['justkapray@gmail.com'], 
    		fail_silently=False)
		return render(request,'signups/signups.html')

def designers(request):
	return render(request, 'signups/designers.html')
	
def shopfront(request):
	return render(request, 'signups/shopfront.html')

def sellerregiter(request):
	return render(request, 'signups/sellerregister.html')

def buyerregister(request):
	return render(request, 'signups/buyerregister.html')
	
def contact(request):
	
	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		brand = request.POST['brand']
		sample = request.POST['sample']
	return render(request, 'signups/contact.html')

