from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

def login_request(request):
	if request.method=="POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return render(request,"Account/login.html",{
				"error":"username ve parol yanlisdir"
				})

	return render(request,"Account/login.html")
def register_request(request):
	return render(request,"Account/register.html")
def logout_request(request):
	logout(request)
	return redirect("home")