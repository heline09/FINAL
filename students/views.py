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

@login_required
def student_dashboard(request):
    student_skills = request.user.skills.all()
    internships = []

    valid_internships = Internship.get_all()

    for skill in student_skills:
        for internship in skill.internships.filter(id__in=valid_internships):
            if internship not in internships: # to avoid repetition
                internships.append(internship)

    context = {
        'internships': internships,
    }

    return render(request, 'students/student_dashboard.html', context)

@login_required
def applyPage(request, internship_id):
    internship = get_object_or_404(Internship, pk=internship_id)
    existing_application = Application.objects.filter(internship_id=internship_id, applicant=request.user).first() #check for existing application
    
    if internship.can_apply():
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

@csrf_exempt
def generate_report(request):
    if request.method == 'POST':
        # Get data from request
        data = json.loads(request.body)

        # Create PDF using ReportLab
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.drawString(100, 750, "Application Report")  # Add report title
        y = 730
        for row in data['data']:
            y -= 20
            pdf.drawString(100, y, ', '.join(row))  # Add table data
        pdf.showPage()
        pdf.save()

        # Return the PDF as an HttpResponse
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="application_report.pdf"'
        response.write(buffer.getvalue())
        buffer.close()
        return response
    else:
        return HttpResponse(status=400)