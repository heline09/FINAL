from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RecruiterForm
from internconnect.models import Internship,Notification
from accounts.models import Skill, FieldOfStudy
from students.models import Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



@login_required
def recruiter_dashboard(request):
    internships = Internship.objects.filter(recruiter=request.user, candidates__isnull=False)
    notifications = Notification.objects.filter(recipient=request.user) 
    context ={'notifications': notifications, 'internships':internships}
    print(context)
    return render(request, 'recruiters/recruiter_dashboard.html', context)

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
    if request.method=='POST':
        if 'accept' in request.POST:
            application.status = 'Accepted'
            application.save()
        elif 'denied' in request.POST:
            application.status = 'Denied'
            application.save()
        return redirect('applicant_details') # return to applicant details page after responding to the applications
            
    return render(request, 'students/applicant_details.html', {'application':application})
