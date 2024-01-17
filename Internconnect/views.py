from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Internconnect/dashboard.html')

def listings(request):
     return render(request, 'Internconnect/listings.html')

def application(request):
     return render(request, 'Internconnect/application.html')



# Create your views here.
