from django.forms import ModelForm
from django import forms
from internconnect.models import Internship
from accounts.models import Skill, FieldOfStudy
from django.utils import timezone

class RecruiterForm(ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

    class Meta:
        model = Internship
        fields = ['title', 'company', 'description', 'skills', 'start_date', 'end_date', 'expiry_date', 'location', 'requirements', 'max_responses']

