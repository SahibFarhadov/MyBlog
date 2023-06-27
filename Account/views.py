from django.shortcuts import render,redirect
from django.contrib.auth import logout

def login_request(request):
	return render(request,"Account/login.html")
def register_request(request):
	return render(request,"Account/login.html")
def logout_request(request):
	logout(request)
	return redirect("home")