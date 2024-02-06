from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # library for user authentication
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User


def registerPage(request):    
     if request.method == "POST":
          username = request.POST.get('uname')
          email = request.POST.get('email')
          password1 = request.POST.get('pass1')
          password2 = request.POST.get('pass2')
          role = request.POST.get('role')

          # check if username exists

          if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken. Please choose a different one.')
            return redirect('register')  # Redirect back to the registration form

           # check if passwords match
          if password1 != password2:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('register')  # Redirect back to the registration form

            # create new user
          new_user = User.objects.create_user(username, email, password1)
          new_user.save()

          messages.success(request, f'Hi {username}, your account has been created successfully')
          return redirect('signin')

     return render(request, 'accounts/register.html')


def loginPage(request):
     if request.method == "POST":
          username = request.POST.get('uname')
          password = request.POST.get('pass')

          user = authenticate(request, username = username, password = password) # watch out for TypeError here (0 to 1)positiona args..
          if user is not None:                           #if user exists, redirect to homepage
                login(request, user)
                return redirect('/')
          else:
               return HttpResponse('Error: User does not exist')
          
     return render(request, 'accounts/signin.html')  # if absent results into a ValueError HttpResponse Object


def logoutUser(request):
     logout(request)
     return redirect('signin')


def recruiter(request):
     return render(request, 'accounts/recruiter.html') # recruiter registration page



