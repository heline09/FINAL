from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login as auth_login # library for user authentication
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm, EditUserForm, EditStudentProfileForm, EditRecruiterProfileForm
from .models import SubscriptionPlan, UserSubscription, Skill, FieldOfStudy
from internconnect.models import Internship
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import StudentProfile, RecruiterProfile
from django.conf import settings
from django.core.mail import send_mail


def registerPage(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get the selected role from the form or another source
            selected_role = form.cleaned_data.get('role')  # Example

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
            subject = 'Welcome to Internconnect'
            message = f'Hi {user.username}, thank you for joining Internconnect'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail(subject, message, email_from, recipient_list )
            if selected_role == "student":
                return redirect('skills')
            elif selected_role == "recruiter":
                return redirect('subscribePage')
            else:
                # Handle invalid role selection
                messages.error(request, "Invalid role selected.")
                return redirect('register')  # Redirect back to registration form
        else:
            print("Form not valid")
            # Handle form validation errors
            for field, errors in form.errors.items():
                print(errors)
                for error in errors:
                    err_msg = error.capitalize()
                    messages.error(request, err_msg)

    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@login_required
def skillPage(request):
    if request.method == "POST":
        selected_field_of_study_id = request.POST.get("select_field_of_study")
        selected_skills = request.POST.getlist("skills")
        
        for skill_id in selected_skills:
            skill = Skill.objects.get(id=skill_id)
            request.user.skills.add(skill) # Save selected skills for the user
        
        # Render internships on student dashboard
        return redirect('student_dashboard')
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

        return render(request, 'students/skill.html', context)  

    
def subscribePage(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'accounts/subscription.html',{'plans': plans})     
                            
   
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


def student_profile(request, user_id ):
    student_profile = get_object_or_404(StudentProfile,user_id=user_id)
    return render(request, 'accounts/student_profile.html', {'student_profile': student_profile})

def recruiter_profile(request, user_id):
    recruiter_profile = get_object_or_404(RecruiterProfile, user_id=user_id)
    user_subscription = recruiter_profile.user.subscribed.first()
    context = {
    'recruiter_profile': recruiter_profile,
    'end_date': user_subscription.end_date if user_subscription else None
}
    return render(request, 'accounts/recruiter_profile.html', context)

def edit_profile(request):
    student_profile = StudentProfile.objects.get(user=request.user)
   #recruiter_profile = RecruiterProfile.objects.
    if request.method =='POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        print("POST request received")

        if(request.user, 'student.profile'):
            profile_form = EditStudentProfileForm(request.POST, request.FILES, instance=request.user)
        else:
            profile_form = EditRecruiterProfileForm(request.POST, request.FILES, instance=request.user)
            print("User form is valid:", user_form.is_valid())
            print("Prof form is valid:", profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if(request.user, 'student.profile'):
                return redirect('student_profile', user_id=request.user.id)  # Redirect to student profile
            else:
                return redirect('recruiter_profile', user_id=request.user.id)  # Redirect to recruiter 
                
    else:
        user_form = EditUserForm(instance=request.user)
        # Check if the user is student or recruiter based on their profile existence
        if(request.user, 'student.profile'):
            profile_form = EditStudentProfileForm(instance=request.user)
        else:
            profile_form = EditRecruiterProfileForm(instance=request.user)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/edit_profile.html', context)

    # if request.method=='POST':
    #     user_form = EditUserForm(request.POST, instance=request.user)
    #     if hasattr(request.user, 'student_profile'):
    #         profile_form = EditStudentProfileForm(request.POST, request.FILES, instance=request.user)
    #         if user_form.is_valid() and profile_form.is_valid():
    #           user_form.save()
    #           profile_form.save()
    #           messages.success(request, f'Your details have been updated successfully')
    #           return redirect('student_profile', user_id)

    # else:
    #     user_form = EditUserForm(instance=request.user)
    #     if hasattr(request.user, 'student_profile'):
    #         profile_form = EditStudentProfileForm(instance=request.user.student_profile)
    # context = {'user_form': user_form}
        
    # return render (request, 'accounts/edit_profile.html', context)





