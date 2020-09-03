from django.shortcuts import render
from django.http import HttpResponse

"""Views to handle requests to the polls app"""

def index(request):
	return HttpResponse("This is the polls index page")
