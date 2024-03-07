from django.contrib import admin
from .models import CustomUser, StudentProfile, RecruiterProfile, UserSubscription, SubscriptionPlan, FieldOfStudy, Skill, Student


# Register your models here.
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(FieldOfStudy)
admin.site.register(Student)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

@admin.register(RecruiterProfile)
class RecuiterProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'role']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
