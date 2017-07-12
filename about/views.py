from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext, loader
from datetime import datetime
# Create your views here.

def about(request):
	return render(request, 'about/about.html')