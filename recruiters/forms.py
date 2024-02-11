from django.forms import ModelForm
from django import forms
from internconnect.models import Internship

class RecruiterForm(ModelForm):
    title = forms.TextInput
    company = forms.TextInput
    description = forms.Textarea
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.TextInput
    requirements = forms.Textarea
    class Meta:
        model = Internship
        fields = ['title', 'company', 'description', 'start_date', 'end_date', 'location', 'requirements']

