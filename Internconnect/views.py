from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Internship
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .methods import handle_pagination

def listings(request):
     internships = Internship.objects.all()  # Retrieve all internship objects
     page = handle_pagination(request, internships, per_page=10)
     return render(request, 'internconnect/listings.html', {'internships': page.object_list, "page": page})

    # setup pagination
   
def render_content(request):             # this is the content I'm trying to render in the first app
    internships = Internship.objects.all()
    context = {'internships': internships}
    print(context)
    return render(request, 'internconnect/content.html', context)

def home(request):
    return render(request, 'internconnect/landing.html')

def application(request):
     return render(request, 'internconnect/application.html')

def details(request, internship_id):
     internship = get_object_or_404(Internship, pk=internship_id)
     return render(request, 'internconnect/details.html', {'internship':internship})

# Create your views here.
