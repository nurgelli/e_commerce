from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.username
    
class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
        ("P", "Prefer not say"),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True, null=True)
    marketing_opt_in = models.BooleanField(default=False)
    currency_preference = models.CharField(max_length=10, blank=True)
    language_preference = models.CharField(max_length=10, blank=True)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"Profile of {self.user.username}"
    


