from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login # library for user authentication
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm, StudentForm
from .models import SubscriptionPlan, UserSubscription, Student, Skill, FieldOfStudy
from internconnect.models import  SelectedSkill, Internship


# def registerPage(request):  
#      form = UserRegisterForm()  
#      if request.method == "POST":
#           form = UserRegisterForm(request.POST)
#           if form.is_valid():
#                CustomUser = form.save()
#                username = form.cleaned_data.get('username')
#                messages.success(request, f'Account created successfully for {username}, you can now login') 
#                return redirect('skill')    
#           else: 
#                for field, errors in form.errors.items():
#                     for error in errors:
#                          err_msg = error.capitalize()
#                          messages.error(request, err_msg)       
#      elif request.method == "GET":
#           if request.user.is_authenticated:
#                return redirect('/')
         
#      context = {'form': form}
#      return render(request, 'accounts/register.html', context)
def registerPage(request):

    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get the selected role from the form or another source
            selected_role = form.cleaned_data.get('role')  # Example
            if selected_role == "student":
                return redirect('skills')
            elif selected_role == "recruiter":
                return redirect('subscription_plans')
            else:
                # Handle invalid role selection
                messages.error(request, "Invalid role selected.")
                return redirect('register')  # Redirect back to registration form
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    err_msg = error.capitalize()
                    messages.error(request, err_msg)

    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def skillPage(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_field_of_study_id = request.POST.get("select_field_of_study")
            skills = request.POST.getlist("skills")
            internships = Internship.objects.all()

            internships = []
            for internship in internships:
                required_skills = internship.skills.all()
                if all(skill_id in skills for skill_id in required_skills):
                    matches.append(internship)
                    
            # Save selected skills for the user
            if skills:
                for skill_id in skills:
                    request.user.skills.add(Skill.objects.get(id=skill_id))

            # Render internships on student dashboard
            return render(request, 'students/student_dashboard.html', {'internships': internships})
        else:
            select_options = {}
            for field in FieldOfStudy.objects.all():
                skills = [{'id': skill.id, 'name': skill.name} for skill in field.skills.all()]
                select_options[field.id] = skills    

            selected_field_of_study_id = request.POST.get("select_field_of_study")
            if selected_field_of_study_id:
                skills = Skill.objects.filter(fields_of_study_id=selected_field_of_study_id)
            else:
                skills = Skill.objects.all()

            context = {
                'fields_of_study': FieldOfStudy.objects.all(),
                'select_options': select_options,
                'skills': skills
            }

            return render(request, 'accounts/skill.html', context)  
    else:
        return redirect('register')

       
       
          

def subscription_plans(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'accounts/subscription_plans.html', {'plans': plans})

def choose_subscription(request, plan_id):
    plan = SubscriptionPlan.objects.get(pk=plan_id)
   
    return redirect('/') # redirect to landing page

def user_subscriptions(request):
    user_subscriptions = UserSubscription.objects.filter(user=request.user)
    return render(request, 'accounts/user_subscriptions.html', {'subscriptions': user_subscriptions})


def loginPage(request):
     username = ''
     password = ''
     if request.method == "POST":
          username = request.POST.get("username", '')
          password = request.POST.get("password", '')

          user = authenticate(request, username = username, password = password) # watch out for TypeError here (0 to 1)positiona args..
          if user is not None:                           #if user exists, redirect to homepage
                auth_login(request, user)
                if user.role == 'recruiter':
                    return redirect('recruiter_dashboard')
                elif user.role == 'student':
                    return redirect('student_dashboard')
                elif user.role == 'admin':
                    return redirect('admin_dashboard')
          else:
              messages.error(request, 'Username or Password is incorrect')
     elif request.method =="GET":
         if request.user.is_authenticated:
              return redirect('/')     
     context = {'username': username, 'password':password}
     return render(request, 'accounts/login.html')  # if absent results into a ValueError HttpResponse Object


def logoutUser(request):
     logout(request)
     return redirect('/')





