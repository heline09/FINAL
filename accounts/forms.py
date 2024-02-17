from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import SubscriptionPlan

User = get_user_model()

class UserRegisterForm(UserCreationForm):
     subscription_plan = forms.ModelChoiceField(queryset=SubscriptionPlan.objects.all(), label='Select Subscription Plan')

     class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'subscription_plan']

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs['onchange'] = 'showSubscriptionPlan()'

def clean(self):
    cleaned_data = super().clean()
    role = cleaned_data.get('role')
    subscription_plan = cleaned_data.get('subscription_plan')

    if role == 'recruiter' and not subscription_plan:
        raise forms.ValidationError("Recruiters must select a subscription plan")

    return cleaned_data