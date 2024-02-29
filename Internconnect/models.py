from django.db import models
from accounts.models import CustomUser, Skill
from django.utils import timezone

class Internship(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    post_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(blank=True, null=True)
    location = models. CharField(max_length=50)
    requirements = models.TextField()
    recruiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="internships")
    skills = models.ManyToManyField(Skill, related_name='internships')
    

    def __str__ (self):
        return self.title
        
class SelectedSkill(models.Model):
     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
     skills = models.ManyToManyField(Skill)

     def __str__(self):
        return self.user.username

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='notifications')
    message = models.TextField()


    def __str__(self):
        return f"Notification to {self.recipient.username} - {self.message}"
        
# Create your models here.
