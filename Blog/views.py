from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Category
from django.views.generic.edit import CreateView

class BlogCreationView(CreateView):
	model=Blog
	fields=["title","image","description","category","is_active","is_home"]

def home(request):
	blogs=Blog.objects.all()
	categories=Category.objects.all()
	context={
		"blogs":blogs,
		"categories":categories
	}
	return render(request,"blog/index.html",context)

def blogs(request):
	blogs=Blog.objects.all()
	categories=Category.objects.all()
	context={
		"blogs":blogs,
		"categories":categories
	}
	return render(request,"blog/blogs.html",context)

def blog_details(request,_slug):
	blog=Blog.objects.get(slug=_slug)
	context={
		"blog":blog
	}
	return render(request,"blog/blog-details.html",context)

def blogs_by_category(request,_slug):
	categories = Category.objects.all()
	selectedCategory=Category.objects.get(slug=_slug)
	blogs=Blog.objects.filter(category__slug=_slug)
	context={
		"blogs":blogs,
		"categories":categories,
		"selectedCategory":selectedCategory
	}
	return render(request,"blog/blogs_by_category.html",context)

def meqale_yaz(request):
	return render(request,'blog/meqale_yaz.html')