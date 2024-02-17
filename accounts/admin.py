from django.contrib import admin
from .models import CustomUser, UserProfile, UserSubscription, SubscriptionPlan


# Register your models here.
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(UserProfile)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']