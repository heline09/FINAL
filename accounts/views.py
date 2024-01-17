from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request, 'accounts/register.html')

def signin(request):
    return render(request, 'accounts/signin.html')


# Create your views here.
