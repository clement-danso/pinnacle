from django.shortcuts import render

# Create your views here.
def home(request):
	
	
	
	return render(request, 'pinapp/index.html')


def contact(request):
	
	
	return render(request, 'pinapp/contact.html')
	
	
def company(request):
	
	
	
	return render(request, 'pinapp/company.html')
	
def resources(request):
	
	
	
	return render(request, 'pinapp/resources.html')
