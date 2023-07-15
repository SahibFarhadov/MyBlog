from django.urls import path
from . import views

urlpatterns=[
	path('daxil_ol',views.login_request,name='login'),
	path('qeydiyyatdan_kec',views.register_request,name='register'),
	path('hesabdan_cix',views.logout_request,name='logout'),
	path("menim_hesabim/<_username>",views.hesab,name="profile")
]