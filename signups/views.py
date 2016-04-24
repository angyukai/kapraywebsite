from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.template import loader
from forms import SignUpForm
from models import Designer
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
		
 		designer = Designer.objects.create(name=name, email=email, brand = brand, sample = sample)
		designer.save()
		
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
	return render(request, 'signups/contact.html')

