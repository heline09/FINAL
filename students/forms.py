from django.forms import ModelForm
from django import forms
from internconnect.models import Internship
from .models import Application
from accounts.models import Skill, FieldOfStudy
from django.utils import timezone

class ApplicationForm(ModelForm):
    cv = forms.FileField(label='My CV', help_text='Upload your CV (PDF, DOC, DOCX)')
    application_message = forms.CharField(label='My Application Message', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), help_text='Enter your application message here')

    
    def clean_cv(self):
        cv = self.cleaned_data['cv']
        if cv:
            # Get the file extension
            ext = cv.name.split('.')[-1].lower()
            # Check if the file extension is allowed
            if ext not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError('Only PDF, DOC, and DOCX files are allowed.')
        return cv

    class Meta:
        model = Application
        fields = ['cv', 'application_message']
