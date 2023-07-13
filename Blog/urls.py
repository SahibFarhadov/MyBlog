from django.urls import path
from . import views
from django.views.generic.edit import CreateView


urlpatterns=[
	path("",views.home,name="home"),
	path("esas",views.home),
	path("meqaleler",views.blogs,name="blogs"),
	path("meqale/<slug:_slug>",views.blog_details,name="blog-details"),
    path("kateqoriya/<slug:_slug>",views.blogs_by_category,name="blogs_by_category"),
    path("meqale_yaz",views.BlogCreateView.as_view(),name="meqale_yaz"),
    path("meqale/yenile/<slug>/",views.BlogUpdateView.as_view(),name="meqale_yenile")
]