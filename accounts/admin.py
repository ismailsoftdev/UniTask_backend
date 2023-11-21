from django.contrib import admin
from django.utils.html import format_html
from .models import User
from accounts.forms import UserForm

@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'profile_image',
                    'is_superuser', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)
    form = UserForm
    
    def profile_image(self, obj):
        if obj.profile:
            return format_html('<img src="{}" width="40" height="40" />'.format(obj.profile.url))
        else:
            return format_html('<img src="{}" width="40" height="40" />'.format('https://www.seekpng.com/png/detail/110-1100707_person-avatar-placeholder.png'))
