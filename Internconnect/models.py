from django.db import models
from accounts.models import Student, CustomUser, Skill
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
    candidates = models.ManyToManyField(CustomUser, related_name='applied_internships')

    def __str__(self):
        return self.title

# class InternshipApplication(models.Model):
#     internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
#     student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     accepted = models.BooleanField(default=False)

#     class Meta:
#         unique_together = (('internship', 'student'),)

# class Intern(model.Models):
#     application = models.ForeignKey(InternshipApplication, on_delete=CASCADE)
#     accepted_date= models.DateField(auto_now_add=True)


   
    
    # @classmethod
    # def get_all(cls):
    #     return cls.objects.filter(expiry_date__gte=date.today())



        
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='notifications')
    message = models.TextField()
    opened = models.BooleanField(default=False)


    def __str__(self):
        return f"Notification to {self.recipient.username} - {self.message}"
        
# Create your models here.
