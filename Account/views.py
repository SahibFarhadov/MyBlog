from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

#account app ucun login metodu
def login_request(request):
	if request.user.is_authenticated:
		return redirect("home")
	if request.method=="POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return render(request,"Account/login.html",{
				"error":"İstifadəçi adı və ya parol yanlışdır"
				})
	return render(request,"Account/login.html")

# account app ucun register metodu
def register_request(request):
	if request.user.is_authenticated:
		return redirect('home')
	return render(request,"Account/register.html")

#account app ucun logout metodu
def logout_request(request):
	logout(request)
	return redirect("home")