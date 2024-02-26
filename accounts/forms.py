from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Student, Skill, FieldOfStudy
from django.forms import ModelForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):

     class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']


class StudentForm(ModelForm):
     fields_of_study = forms.ModelChoiceField(queryset=FieldOfStudy.objects.all(), label='Select your field')
     skill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple, label='Select your skills')

     class Meta:
        model = Student
        fields = ['fields_of_study', 'skill']

