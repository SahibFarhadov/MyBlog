from django.shortcuts import render,redirect
from .models import Blog,Category
from django.views.generic.edit import CreateView,UpdateView
from .forms import AddBlogForm
from django.contrib.auth.models import User
from Account import views as account_views
from django.core.exceptions import ObjectDoesNotExist


class BlogUpdateView(UpdateView):
	model=Blog
	fields=["titleofblog","image","description","is_active","is_home","category",]
	template_name="Blog/meqale_yenile.html"

	def dispatch(self,request,*args,**kwargs):
		if not request.user.is_authenticated:
			return redirect("login")
		return super().dispatch(request,*args,**kwargs)

class BlogCreateView(CreateView):
	model=Blog
	template_name="Blog/meqale_yaz.html"
	form_class=AddBlogForm
	success_url="/hesab/hesab-meqaleleri"
	def form_valid(self,form):
		form.instance.user=self.request.user.myuser
		return super().form_valid(form)

	def dispatch(self,request,*args,**kwargs):
		if not request.user.is_authenticated:
			return redirect("login")
		return super().dispatch(request,*args,*kwargs)

def delete_blog(request,_slug):
	if request.user.is_authenticated:
		try:
			blog=Blog.objects.get(slug=_slug)
			if blog.user == request.user.myuser:
				blog.delete()
		except ObjectDoesNotExist:
			return account_views.hesab_meqaleleri(request)
	return account_views.hesab_meqaleleri(request)


def home(request):
	blogs=Blog.objects.all()
	categories=Category.objects.all()
	context={
		"blogs":blogs,
		"categories":categories
	}
	return render(request,"blog/index.html",context)

def blog_details(request,_slug):
	blog=Blog.objects.get(slug=_slug)
	userBlog=None
	if blog.user is not None:
		userBlog=blog.user.user
	context={
		"blog":blog,
		"userBlog":userBlog
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