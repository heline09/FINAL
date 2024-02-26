from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RecruiterForm
from internconnect.models import Internship
from accounts.models import Skill, FieldOfStudy
from django.contrib.auth.decorators import login_required


@login_required
def recruiter_dashboard(request):
    notifications = request.user.notifications.all() 
    context ={'notifications': notifications}
    print(context)
    return render(request, 'recruiters/recruiter_dashboard.html', context)

def posts(request): 
    context = {}
    
    if request.method == 'POST':
        form = RecruiterForm(request.POST or None)
        if form.is_valid(): 
            fields_of_study = form.cleaned_data['fields_of_study'] 
            selected_field_of_study_id = fields_of_study.id 
            skills = Skill.objects.filter(fields_of_study_id=selected_field_of_study_id) 
            context['skills'] = skills 
            internship = form.save(commit=False) 
            internship.recruiter = request.user 
            internship.save() 
            messages.success(request, 'Your form is submitted successfully!') 
            return redirect('recruiter_dashboard') 
    else: 
        form = RecruiterForm() 

    select_options = {} 
    for field in FieldOfStudy.objects.all(): 
        skills = [] 
        for skill in field.skills.all(): 
            skills.append({'id':skill.id, 'name':skill.name}) 
        select_options[field.id] = skills 

    context['fields_of_study'] = FieldOfStudy.objects.all() 
    context['select_options'] = select_options 
    context['skills'] = Skill.objects.all() 
    context['form'] = form 

    return render(request, 'recruiters/posts.html', context)


def posted(request): # logic for the posted jobs tab
    internships = Internship.objects.all() #query the database
    return render(request, 'recruiters/posted.html', {'internships': internships}) # for the posted internships by a certain revruiter


# Create your views here.
