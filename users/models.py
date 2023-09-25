from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # Add custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name="userprofile_set",
        related_query_name="userprofile",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name="userprofile_set",
        related_query_name="userprofile",
    )


class UserPreferences(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    preferred_spot_type = models.CharField(max_length=100, blank=True)
    notification_frequency = models.CharField(max_length=100, blank=True)
    privacy_settings = models.TextField(blank=True)
