from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RecruiterForm
from internconnect.models import Internship, Notification
from accounts.models import Skill, FieldOfStudy
from students.models import Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
import mimetypes
#xhtml imports
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context



@login_required
def recruiter_dashboard(request):
    internships = []
    for internship in Internship.objects.filter(recruiter=request.user):
        if internship.applications.count() > 0:
            internships.append(internship)
    notifications = Notification.objects.filter(recipient=request.user) 
    context ={'notifications': notifications, 'internships':internships}
    print(context)
    return render(request, 'recruiters/recruiter_dashboard.html', context)

@login_required
def posts(request): 
    context = {}
    
    if request.method == 'POST':
        form = RecruiterForm(request.POST or None)
        if form.is_valid(): 
            internship = form.save(commit=False) 
            internship.recruiter = request.user 
            internship.save() 
            selected_skills = request.POST.getlist("skills")      
            for skill_id in selected_skills:
               skill = Skill.objects.get(id=skill_id)
               internship.skills.add(skill) # Save selected skills for the internship
           
          
            messages.success(request, 'Your form is submitted successfully!') 
            return redirect('recruiter_dashboard') 
        else:
            print(form.errors)
    else: 
        form = RecruiterForm() 
       

    select_options = {} 
    for field in FieldOfStudy.objects.all():
            skills = [{'id': skill.id, 'name': skill.name} for skill in field.skills.all()]
            select_options[field.id] = skills    

    selected_field_of_study_id = request.POST.get("select_field_of_study")
    if selected_field_of_study_id:
               skills = Skill.objects.filter(fields_of_study_id=selected_field_of_study_id)
    else:
              skills = Skill.objects.all()

    context['fields_of_study'] = FieldOfStudy.objects.all() 
    context['select_options'] = select_options 
    context['skills'] = Skill.objects.all() 
    context['form'] = form 
    return render(request, 'recruiters/posts.html', context)

def posted(request):
    internships = Internship.objects.filter(recruiter=request.user) 
    return render(request, 'recruiters/posted.html', {'internships': internships}) 

def applicant_list(request, internship_id):
    internship = get_object_or_404(Internship, pk=internship_id)
    applications = Application.objects.filter(internship=internship)
    return render(request, 'recruiters/applicant_list.html', {'internship': internship, 'applications': applications})

def applicant_details(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    print(application.status)
    applicant = application.applicant
    if request.method=='POST':
        if 'accepted' in request.POST:
            application.status = 'accepted'
            application.save()
        elif 'denied' in request.POST:
            application.status = 'denied'
            application.save()

            applicant_notification_message = f"Your application for '{application.internship.title}' has been {application.status.upper()}."

            Notification.objects.create(
                recipient=application.applicant,
                message=  applicant_notification_message 
                          )
       
        send_application_status_notification(application)    
        return redirect('applicant_list', internship_id=application.internship.id) # return to applicants page after responding to the applications
            
    return render(request, 'students/applicant_details.html', {'application':application})

def update_internship(request, id):
    internship = Internship.objects.get(id=id)
    
    if request.method == 'POST':
        # Handle form submission for editing
        form = RecruiterForm(request.POST, instance=internship)  # Pre-populate the form
        if form.is_valid():
            form.save()
            messages.success(request, 'Your internship is updated and submitted successfully!') 
            return redirect('recruiter_dashboard')  # Replace with appropriate URL
    else:
        # Display the editing form with existing data
        form = RecruiterForm(instance=internship)  # Pre-populate the form
    
    # Fetch all fields of study and their associated skills
    select_options = {}
    for field in FieldOfStudy.objects.all():
        skills = [{'id': skill.id, 'name': skill.name} for skill in field.skills.all()]
        select_options[field.id] = skills

    # Get the selected field of study ID from the POST data
    selected_field_of_study_id = request.POST.get("select_field_of_study")

    # If a field of study is selected, filter skills based on it; otherwise, fetch all skills
    if selected_field_of_study_id:
        skills = Skill.objects.filter(fields_of_study_id=selected_field_of_study_id)
    else:
        skills = Skill.objects.all()
    # Populate context with necessary data
    context = {
        "internship": internship,
        "form": form,
        "fields_of_study": FieldOfStudy.objects.all(),  # Maintain existing context
        "select_options": select_options,  # Pass select options to the template
        "skills": skills,  # Pass skills based on the selected field of study
    }
          
    return render(request, 'recruiters/updateform.html', context)

def deactivate_internship(request, internship_id):
    internship = Internship.objects.get(pk=internship_id)
    internship.is_active = False
    internship.save()

    return redirect('posted')

def confirmation_status_check(request, application_id):
    # confirmed_applications = Application.objects.filter(is_confirmed=True)
    application = get_object_or_404(Application, pk=application_id)
    if application.status == 'accepted':
        application.is_confirmed = True
        application.internship.is_complete = True
        application.internship.save()
        application.save()
        messages.success(request, 'Successfully Confirmed.')
    else:
        messages.error(request, 'Sorry, your application has not been accepted')
    
    return redirect('student_dashboard')  

def send_application_status_notification(application):
  subject = f"Your Internship Application for {application.internship.title} - {application.status.upper()}"
  message = f"Dear {application.applicant.username},\n"
  if application.status == 'accepted':
    message += f"Congratulations! Your application for the internship '{application.internship.title}' has been accepted."
  elif application.status == 'denied':
    message += f"We regret to inform you that your application for the internship '{application.internship.title}' has been denied."
  message += "\n\nRegards,\nThe Internconnect Team"
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [application.applicant.email,]
  send_mail(subject, message, email_from, recipient_list)

def download_cv(request, application_id):
    try:
     application = get_object_or_404(Application, pk=application_id)
     cv_file = application.cv

     response = HttpResponse(cv_file, content_type='application/pdf')
     response['Content-Disposition'] = 'attachment; filename="cv.pdf"'  # Change filename as per your file name

     return response
    except (Application.DoesNotExist, FileNotFoundError):
        messages.error(request, 'CV not found.')
        return redirect('applicant_details', application_id)

def generate_pdf_report(request):
    internships = Internship.objects.filter(recruiter=request.user) 
    template_path = 'recruiters/posted_report.html'  # Path to your HTML template

    # Get the current date
    today_date = date.today().strftime("%B %d, %Y")
    logo_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'org(3).png')
    
    context = {
        'internships': internships,
        'logo_path': logo_path,
         'date': today_date
    }
    # Render template
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="internship_report.pdf"'

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='utf-8')

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response