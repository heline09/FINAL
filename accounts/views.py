from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.http import HttpResponse

def registerPage(request):
    return render(request, 'accounts/register.html')

def student(request):
     if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, user)
            #messages.success(request, 'Registration succesful!')
            return HttpResponse(request, 'accounts/signin.html')  
     else:
        form =CreateUserForm()

        return render(request, 'accounts/student.html', {'form': form})

def recruiter(request):
     return render(request, 'accounts/recruiter.html') # recruiter registration page

def loginPage(request):
     return render(request, 'accounts/signin.html')


