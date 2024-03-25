from django.forms import ModelForm
from django import forms
from internconnect.models import Internship
from accounts.models import Skill, FieldOfStudy
from django.utils import timezone
from datetime import date

class RecruiterForm(ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

    class Meta:
        model = Internship
        fields = ['title', 'company', 'description', 'skills', 'start_date', 'end_date', 'expiry_date', 'location', 'requirements', 'max_responses']

    def clean_start_date(self):
        data = self.cleaned_data['start_date']
        if data < date.today():
            raise forms.ValidationError("Start date cannot be in the past. Please choose a future date.")
        return data

    def clean_end_date(self):
        data = self.cleaned_data['end_date']
        if data < date.today():
            raise forms.ValidationError('End date cannot be in the past. Pick a future date')
        return data

    def clean_expiry_date(self):
        data = self.cleaned_data['expiry_date']
        if data < date.today():
            raise forms.ValidationError('Expiry date cannot be in the past. PLease pick a future date')
        return data