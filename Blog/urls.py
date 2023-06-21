from django.urls import path
from . import views

urlpatterns=[
	path("",views.home,name="home"),
	path("index",views.home),
	path("blogs",views.blogs,name="blogs"),
	path("blogs/<slug:_slug>",views.blog_details,name="blog-details"),
    path("category/<slug:_slug>",views.blogs_by_category,name="blogs_by_category")
]