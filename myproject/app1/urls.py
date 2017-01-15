from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^bussearch$', views.bussearch, name = "test"),
	# url(r'^addlist$', views.crtable, name = "add"),
	url(r'^signup',views.signup, name = "signup"),
	url(r'^login$',views.login, name = "login"),
	url(r'bussearch',views.bussearch, name = "bussearch"),
	url(r'^logout',views.logout, name = "logout")
]