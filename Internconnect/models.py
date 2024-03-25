from django.db import models
from accounts.models import CustomUser, Skill
from django.utils import timezone
from datetime import date

class Internship(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    post_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50)
    requirements = models.TextField()
    recruiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posted_internships")
    skills = models.ManyToManyField(Skill, related_name='internships')
    max_responses = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)
    # candidates = models.ManyToManyField(CustomUser, related_name='applied_internships')

    def __str__(self):
        return self.title
     
   
    @classmethod
    def get_all(cls):
        return cls.objects.filter(is_complete=False, is_active=True, expiry_date__gte=date.today())
    
    def can_apply(self):
        application_count = self.applications.count()
        return application_count < self.max_responses

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='notifications')
    message = models.TextField()
    opened = models.BooleanField(default=False)


    def __str__(self):
        return f"Notification to {self.recipient} - {self.message}"
        

