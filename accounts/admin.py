from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ['user']
    search_fields = ['user__first_name', 'user__last_name']