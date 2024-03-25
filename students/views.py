from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from internconnect.models import Internship,Notification
from accounts.models import Skill, CustomUser
from .models import Application
from django.contrib.auth.decorators import login_required
import requests
from .forms import ApplicationForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import date
#xhtml imports
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context
from django.conf import settings

@login_required
def student_dashboard(request):
    student_skills = request.user.skills.all()
    active_internships = []

    for skill in student_skills:
        for internship in skill.internships.filter(is_active=True): # Filter only active internships
            if internship not in active_internships: # to avoid repetition
                active_internships.append(internship)

    context = {
        'internships': active_internships,
    }

    return render(request, 'students/student_dashboard.html', context)

@login_required
def applyPage(request, internship_id):
    internship = get_object_or_404(Internship, pk=internship_id)
    existing_application = Application.objects.filter(internship_id=internship_id, applicant=request.user).first() #check for existing application
    # filled_application = Application.objects.filter(internship_id=internship_id, status__in=['accepted']).exists()

    # if filled_application:
    #     messages.error(request, "Sorry, this internship has already been filled.")
    #     return redirect('student_dashboard')

    if not internship.can_apply():
        messages.error(request, 'Maximum response limit reached for this internship.')
        return redirect('student_dashboard')

    if request.method =='POST':
        if existing_application:
            messages.error(request,'You have an existing application')
            return redirect('MyApplications')
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            cv_file = form.cleaned_data['cv']
            application_message= request.POST.get('application_message')
            application.internship = internship  # Assign the selected internship to the application
            application.applicant = request.user
            application.status = 'pending'
            application.save()   
            messages.success(request, 'Your application is submitted successfully!')  

            applicant_notification_message = f"Your application for {internship.title} has been submitted."
            recruiter_notification_message = f"You have received an application for {internship.title}."


            Notification.objects.create(
            recipient=request.user,
            message=applicant_notification_message
            )
            
            Notification.objects.create(
            recipient=internship.recruiter,
            message=recruiter_notification_message
            )
            
            return redirect('MyApplications')
        else:
            print("Form not valid")
    else:
        form = ApplicationForm()
       
    return render(request, 'students/apply.html', {'form':form})

def MyApplications(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'students/application.html', {'applications':applications})
            
@csrf_exempt
def mark_as_read(request, notification_id):
    print("Mark as read", notification_id)
    notification = Notification.objects.get(id=notification_id)
    notification.opened = True
    notification.save()
    return JsonResponse({'success': True})  # Or a custom response

def generate_report(request):
    applications = Application.objects.filter(applicant=request.user) 
    template_path = 'students/applied_report.html'  # Path to your HTML template

    # Get the current date
    today_date = date.today().strftime("%B %d, %Y")
    logo_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'org(3).png')
    
    context = {
        'applications': applications,
        'logo_path': logo_path,
         'date': today_date
    }
    # Render template
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="application_report.pdf"'

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='utf-8')

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response