from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add additional fields in here
    profile = CloudinaryField('Profile Picture', null=True, blank=True)
    
    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'
        
    def __str__(self):
        return f"{self.user.get_full_name()}"
