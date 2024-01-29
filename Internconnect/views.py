from django.shortcuts import render, redirect
from django.contrib import messages
 
def home(request):
    return render(request, 'internconnect/dashboard.html')

def listings(request):
     return render(request, 'internconnect/listings.html')

def application(request):
     return render(request, 'internconnect/application.html')

def description(request):
     return render(request, 'internconnect/description.html')

# Create your views here.
