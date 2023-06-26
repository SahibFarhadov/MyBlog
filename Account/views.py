from django.shortcuts import render

def login_request(request):
	return render(request,"Account/login.html")
def register_request(request):
	return render(request,"Account/login.html")
def logout_request(request):
	return redirect("home")