from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

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
	if request.method=="POST":
		# qeydiyyat formundan melumatlarin alinmasi
		name=request.POST["name"]
		surname=request.POST["surname"]
		nickname=request.POST["nickname"]
		email=request.POST["email"]
		password=request.POST["password"]
		repassword=request.POST["repassword"]

		errorMessage=""
		dataKeep={
			"name":name,
			"surname":surname,
			"nickname":nickname,
			"email":email,
			"errorMessage":errorMessage
		}
		if password==repassword:
			if User.objects.filter(username=nickname).exists():
				dataKeep["errorMessage"]="Daxil edilən istifadəçi adı artıq mövcuddur"
				return render(request, "Account/register.html", dataKeep )
			elif User.objects.filter(email=email).exists():
				dataKeep["errorMessage"]="Daxil edilən email ünvanı artıq istifadə edilmişdir"
				return render(request, "Account/register.html", dataKeep )
			else:
				User.objects.create_user(username=nickname,first_name=name,last_name=surname,password=password,email=email)
				newUser=User.objects.get(username=nickname)
				newUser.is_active=False
				newUser.save()
				return redirect("login")

	return render(request,"Account/register.html")

#account app ucun logout metodu
def logout_request(request):
	logout(request)
	return redirect("home")