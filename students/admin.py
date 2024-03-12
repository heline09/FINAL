from django.contrib import admin
from .models import Application

# admin.site.register(Application)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'internship']
# Register your models here.
