from django.db import models
from accounts.models import User 

class Internship(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models. CharField(max_length=50)
    requirements = models.TextField()


    def __str__ (self):
        return self.title
        


class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    applicant = models. ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])

    
    def __str__ (self):
       return f"{self.applicant.username} - {self.internship.title} - {self.status}"
        
# Create your models here.
