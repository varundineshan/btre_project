from django.shortcuts import render

# Create your views here.
def index(request):
	template_name="listings/listings.html"
	return render(request,template_name)

def listing(request):
	template_name="listings/listing.html"
	return render(request,template_name)

def search(request):
	template_name="listings/search.html"
	return render(request,template_name)