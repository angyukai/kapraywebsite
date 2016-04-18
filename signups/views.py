from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.template import loader
from forms import SignUpForm
from models import User
# from models import CustomerUser

# Create your views here.

def home(request):
    
    return render(request, 'signups/signups.html')
    
def signup(request):
	
	print 'hellohello1'
    
	if request.method == 'POST':
		print 'hellohello2'
		name = request.POST['name']
		email = request.POST['email']
 		user = User.objects.create_user(username=name, email=email)
		user.save()
		
		
		return render(request,'signups/signups.html')

def designers(request):
	return render(request, 'signups/designers.html')
	
def shopfront(request):
	return render(request, 'signups/shopfront.html')

