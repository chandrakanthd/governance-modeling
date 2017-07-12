
"""
Definition of urls for the app.
"""

from django.conf.urls import  url
from . import views

urlpatterns = [
	#/tree
    url(r'^$', views.index, name='index'),
    url(r'^tree/$', views.home, name='home'),
    url(r'^item/$', views.item, name='item'),
    url(r'^functionalities/$', views.functionalities, name='functionalities'),
    ]
