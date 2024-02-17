from django.contrib import admin
from .models import Internship, Application, Notification


# Register your models here.
# admin.site.register(Internship)
admin.site.register(Application)
admin.site.register(Notification)

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'recruiter_id']

