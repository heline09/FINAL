from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from internconnect.models import Internship
from django.contrib.auth.decorators import login_required
import requests


@login_required
def student_dashboard(request):
    internships = Internship.objects.all()
    context = {'internships': internships}
    return render(request, 'students/student_dashboard.html', context)
