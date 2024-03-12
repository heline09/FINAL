from django.db import models
from accounts.models import CustomUser
from internconnect.models import Internship
from django.core.validators import FileExtensionValidator
from django.conf import settings

class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="applied_applications")
    cv = models.FileField(upload_to= 'cvs/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])
    application_message = models.TextField()

    STATUS_CHOICES = [
        ('accepted', 'Accepted')    ,
        ('pending', 'Pending'),
        ('denied', 'Denied'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    
    def __str__ (self):
       return f"{self.applicant.username} - {self.internship.title} - {self.status}"
