from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Internship
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def internship_list(request):
    internships = Internship.objects.values()  # Retrieve all internships as a list of dictionaries
    return JsonResponse({'internships': list(internships)})


@login_required
def home(request):
    return render(request, 'internconnect/dashboard.html')

def listings(request):
     return render(request, 'internconnect/listings.html')

def application(request):
     return render(request, 'internconnect/application.html')

def details(request):
     return render(request, 'internconnect/details.html')

# Create your views here.
