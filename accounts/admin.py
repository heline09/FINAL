from django.contrib import admin
from .models import CustomUser, UserProfile


# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(UserProfile)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']