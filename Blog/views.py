from django.shortcuts import render,redirect
from .models import Blog,Category
from django.views.generic.edit import CreateView,UpdateView
from .forms import AddBlogForm
from django.contrib.auth.models import User
from Account import views as account_views
from django.core.exceptions import ObjectDoesNotExist


# blog update view
class BlogUpdateView(UpdateView):
	model=Blog
	fields=["titleofblog","image","description","is_active","is_home","category",]
	template_name="Blog/meqale_yenile.html"
	success_url="/hesab/hesab-meqaleleri/"

	def dispatch(self,request,*args,**kwargs):
		if not request.user.is_authenticated:
			return redirect("login")
		return super().dispatch(request,*args,**kwargs)

#blog create view
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

#blog delete function
def delete_blog(request,_slug):
	if request.user.is_authenticated:
		try:
			blog=Blog.objects.get(slug=_slug)
			if blog.user == request.user.myuser:
				blog.delete()
		except ObjectDoesNotExist:
			return account_views.hesab_meqaleleri(request)
	return account_views.hesab_meqaleleri(request)


#home page function
def home(request,pageNumber=1):
	blogs=Blog.objects.filter(is_active=True)
	if pageNumber==1:
		filtered_blogs=blogs[(pageNumber-1)*10:(blogs.count()/pageNumber)*10]
	else:
		filtered_blogs=blogs[(pageNumber-1)*10:(blogs.count()/pageNumber)*10]
		
	categories=Category.objects.all()
	context={
		"blogs":filtered_blogs,
		"categories":categories,
		"objs_length":blogs.count,
		"pageNumber":pageNumber
	}
	return render(request,"Blog/index.html",context)

#blog details function
def blog_details(request,_slug):
	blog=Blog.objects.get(slug=_slug)
	userBlog=None
	if blog.user is not None:
		userBlog=blog.user.user
	context={
		"blog":blog,
		"userBlog":userBlog
	}
	return render(request,"Blog/blog-details.html",context)

#kateqoriyaya gore blog cekme funksiyasi
def blogs_by_category(request,_slug):
	categories = Category.objects.all()
	selectedCategory=Category.objects.get(slug=_slug)
	blogs=Blog.objects.filter(category__slug=_slug,is_active=True)
	context={
		"blogs":blogs,
		"categories":categories,
		"selectedCategory":selectedCategory,
		"objs_length":blogs.count,
	}
	return render(request,"Blog/blogs_by_category.html",context)
