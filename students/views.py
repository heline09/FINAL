from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from internconnect.models import Internship
from accounts.models import Student, Skill
from internconnect.models import Notification
from .models import Application
from django.contrib.auth.decorators import login_required
import requests
from .forms import ApplicationForm
from django.shortcuts import get_object_or_404


@login_required
def student_dashboard(request):
    student_skills = request.user.skills.all()
    internships = []
    for skill in student_skills:
        for internship in skill.internships.all():
            if internship not in internships: # to avoid repetition
                internships.append(internship)

    context = {
        'internships': internships,
    }

    return render(request, 'students/student_dashboard.html', context)


def applyPage(request, internship_id):
    internship = get_object_or_404(Internship, pk=internship_id)

    if request.method =='POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            cv_file = form.cleaned_data['cv']
            # internship_id = form.cleaned_data['internship_id']
            cover_letter = request.POST.get('application_message')
            application.internship = internship  # Assign the selected internship to the application
            application.applicant = request.user
            application.status = 'pending'
            application.save()   
            messages.success(request, 'Your application is submitted successfully!')        
            
            Notification.objects.create(
            recipient=request.user,
            message="Your application has been submitted."
            )
            
            Notification.objects.create(
            recipient=internship.recruiter,
            message="You have received an application."
            )
            
            return redirect('student_dashboard')
        else:
            print("Form not valid")
    else:
        form = ApplicationForm()
        return render(request, 'students/apply.html', {'form':form})


