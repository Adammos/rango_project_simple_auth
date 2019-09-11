from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner! Go to about page: "
		"<a href='/rango/about'>about</a>")

def about(request):
	return HttpResponse("Rango says here is the about page. Go back: "
		"<a href='/rango'>index</a>")
