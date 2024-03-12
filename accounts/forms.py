from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Skill, FieldOfStudy
from django.forms import ModelForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
   

     class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']


