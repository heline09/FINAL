from django.db import models
from accounts.models import CustomUser
from internconnect.models import Internship


class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="applied_applications")
    cover_letter = models.TextField()
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Denied', 'Denied'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    
    def __str__ (self):
       return f"{self.applicant.username} - {self.internship.title} - {self.status}"

class UserApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'application')
# Create your models here.
