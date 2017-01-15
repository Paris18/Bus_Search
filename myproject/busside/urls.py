from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^bussearch$', views.bussearch, name = "test"),
	# url(r'^addlist$', views.crtable, name = "add"),
	url(r'^addlist',views.addlist, name = "addlist"),
	url(r'^seatlist',views.seatlist, name = "seatlist"),
]