from django.contrib import admin
from .models import CustomUser, UserProfile, UserSubscription, SubscriptionPlan, FieldOfStudy, Skill, Student, Payment


# Register your models here.
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(UserProfile)
admin.site.register(FieldOfStudy)
# admin.site.register(Skill)
admin.site.register(Student)
admin.site.register(Payment)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
