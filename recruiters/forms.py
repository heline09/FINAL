from django.forms import ModelForm
from django import forms
from internconnect.models import Internship
from accounts.models import Student, Skill, FieldOfStudy
from django.utils import timezone

class RecruiterForm(ModelForm):
    title = forms.TextInput
    company = forms.TextInput
    description = forms.Textarea
    fields_of_study = forms.ModelChoiceField(queryset=FieldOfStudy.objects.all(), label='Select your field')
    skill = forms.ModelChoiceField(queryset=Skill.objects.all(), label='Select your skills')
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    post_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=timezone.now().date())
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.TextInput
    requirements = forms.Textarea
    
    

    class Meta:
        model = Internship
        fields = ['title', 'company', 'description', 'fields_of_study', 'skill', 'start_date', 'end_date', 'post_date', 'expiry_date', 'location', 'requirements']

