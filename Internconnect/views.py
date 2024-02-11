from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Internship
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def listings(request):
     internships = Internship.objects.all()  # Retrieve all internship objects
     return render(request, 'internconnect/listings.html', {'internships': internships})

    # setup pagination
   
def home(request):
    return render(request, 'internconnect/dashboard.html')

@login_required
def recruiter_dashboard(request):
    # Logic for recruiter dashboard
    return render(request, 'internconnect/recruiter_dashboard.html')

@login_required
def student_dashboard(request):
    # Logic for student dashboard
    return render(request, 'internconnect/student_dashboard.html')


def application(request):
     return render(request, 'internconnect/application.html')

def details(request):
     return render(request, 'internconnect/details.html')

# Create your views here.
