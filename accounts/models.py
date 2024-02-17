from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()  # Duration in days
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address', unique=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    ROLES = (
        ('student', 'Student'),
        ('recruiter', 'Recruiter'),
    )
    role = models.CharField(max_length=100, choices=ROLES, default=ROLES[0])

    USERNAME_FIELD ="username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS =["email"]

class UserSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created: # once user is created, create profile for user
        UserProfile.objects.create(user=instance)

