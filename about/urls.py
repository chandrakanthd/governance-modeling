from django.conf.urls import  url
from . import views

urlpatterns = [
	#/tree
    url(r'^$', views.about, name='about'),
    ]