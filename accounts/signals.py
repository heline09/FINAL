from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, StudentProfile, RecruiterProfile

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            StudentProfile.objects.create(user=instance)
        elif instance.is_recruiter:
            RecruiterProfile.objects.create(user=instance)
    