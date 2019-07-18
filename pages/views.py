from django.shortcuts import render
from . import views
# Create your views here.

def index(request):
	template_name="pages/index.html"
	return render(request,template_name)

def about(request):
	template_name="pages/about.html"
	return render(request,template_name)



