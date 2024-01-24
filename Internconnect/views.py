from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def registerPage(request):
    return render(request, 'accounts/register.html')

def student(request):
     if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #login(request, user)
          #   messages.success(request, 'Registration succesful!')
            return redirect('signin')  
     else:
        form =CreateUserForm()

        return render(request, 'accounts/student.html', {'form': form})
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

def recruiter(request):
     return render(request, 'accounts/recruiter.html') # recruiter registration page

def loginPage(request):
     return render(request, 'accounts/signin.html')

def home(request):
    return render(request, 'Internconnect/dashboard.html')

def listings(request):
     return render(request, 'Internconnect/listings.html')

def application(request):
     return render(request, 'Internconnect/application.html')



# Create your views here.
