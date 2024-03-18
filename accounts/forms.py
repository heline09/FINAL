from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Skill, FieldOfStudy, StudentProfile, RecruiterProfile
from django.forms import ModelForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {  
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Create password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
            }

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class EditStudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('image', 'skills', 'cv')

class EditRecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ('image', 'subscription_plan', 'company_name')

