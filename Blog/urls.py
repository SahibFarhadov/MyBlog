from django.urls import path
from . import views
from django.views.generic.edit import CreateView


urlpatterns=[
	path("",views.home,name="home"),
	path("index",views.home),
	path("blogs",views.blogs,name="blogs"),
	path("blogs/<slug:_slug>",views.blog_details,name="blog-details"),
    path("category/<slug:_slug>",views.blogs_by_category,name="blogs_by_category"),
    #path("meqale_yaz",views.meqale_yaz,name="meqale_yaz")
    path("meqale_yaz",views.BlogCreateView.as_view(),name="meqale_yaz")
]