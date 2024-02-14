from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RecruiterForm
from internconnect.models import Internship
from django.contrib.auth.decorators import login_required

@login_required
def recruiter_dashboard(request):
    # Logic for recruiter dashboard
    return render(request, 'recruiters/recruiter_dashboard.html')

def posts(request): # logic for the posting tab
    if request.POST:
        form = RecruiterForm(request.POST)
        if form.is_valid:
            internship = form.save(commit=False)
            internship.recruiter = request.user
            internship.save()
            messages.success(request, 'Your form is submitted successfully!')
        return redirect('recruiter_dashboard')
    else:
        form = RecruiterForm()        
    return render(request, 'recruiters/posts.html', {'form':RecruiterForm})

def posted(request): # logic for the posted jobs tab
    internships = Internship.objects.all()
    return render(request, 'recruiters/posted.html', {'internships': internships}) # for the posted internships by a certain revruiter


# Create your views here.
