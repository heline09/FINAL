from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login # library for user authentication
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm


def registerPage(request):  
     form = UserRegisterForm()  
     if request.method == "POST":
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               CustomUser = form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created successfully for {username}, you can now login') 
               return redirect('login')    
          else: 
               for field, errors in form.errors.items():
                    for error in errors:
                         err_msg = error.capitalize()
                         messages.error(request, err_msg)       
     elif request.method == "GET":
          if request.user.is_authenticated:
               return redirect('/')
         
     context = {'form': form}
     return render(request, 'accounts/register.html', context)


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
     return redirect('login')


def recruiter(request):
     return render(request, 'accounts/recruiter.html') # recruiter registration page



