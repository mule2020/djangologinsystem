from django.shortcuts import render, redirect
from  django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		
		myuser = User.objects.create_user(username, email, password1)

		myuser.first_name = firstname
		myuser.last_name = lastname

		myuser.save()
		messages.success(request, "your account created!")
		return redirect('signin')

 
	return render(request, 'register.html')

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password1']

		user = authenticate(username=username, password=password1)
		if user is not None:
			login(request, user)
			messages.success(request, "Loggged in successfully!")
			return redirect('index')

		else:
			messages.success(request, "credential combinartion error!")
			return redirect('signin')


	return render(request, 'login.html')


def dashboard(request):
	return render(request, 'home.html')