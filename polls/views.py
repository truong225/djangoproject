from django.shortcuts import render
from django.http import HttpResponse

from mysite.settings import DATABASENAME

# Create your views here.
def index(request):
	return HttpResponse("<h1>Hello Django %s</h1>"%DATABASENAME)

def render_index(request):
	return render(request, "index.html")

def hello(request, number):
	text="<h1>welcome to my app number %s!</h1>"%number
	return HttpResponse(text)