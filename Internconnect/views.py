from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
 # if request.method == 'POST':
     #    username = request.POST['username']
     #    email = request.POST['email']
     #    pass1 = request.POST['pass1']
     #    pass2 = request.POST['pass2']

        
     #    myuser = User.objects.create_user(username, email, pass1)
     #    myuser.first_name = fname
     #    myuser.last_name = lname

     #    myuser.save()

     #    messages.success(request, "Your Account has been successfully created!")

        
     # return render(request, 'accounts/signin.html')


def home(request):
    return render(request, 'internconnect/dashboard.html')

def listings(request):
     return render(request, 'internconnect/listings.html')

def application(request):
     return render(request, 'internconnect/application.html')



# Create your views here.
