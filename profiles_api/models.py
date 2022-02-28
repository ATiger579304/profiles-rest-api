from django.db import models

# Standard Base Classes needed to override/customize the default
# Django User Model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Inherit manager funcrions from this class
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles. This leverages Django Classes
        to create a new user for our custom model."""

    def create_user(self, email, name, password=None):
        """Create a new user profile.
            Email (our username) is required."""
        if not email:
            raise ValueError('User must have an email address')
        """normalize makes all chars after @ lower case"""
        email = self.normalize_email(email)
        """Creates our new model with provided fields"""
        user = self.model(email=email, name=name)
        """This encrypts the typed password as a hash"""
        user.set_password(password)
        """Finally save it to the default database
            Can use specific database here."""
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details
            using our new function above, and give the additional booleans"""
        user = self.create_user(email, name, password)
        """ is_superuser is automatically provided by PermissionsMixin
            We declared is_staff in our custom model."""
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# New class thqt inherits from the 2 classes above
# Triple-Double Quotes is Python Standard for writing doc strings (documentation)
# Recommended under every class to Describe
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    """The fields below are for permissions"""
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """Since we are overriding Django's manager
        We must provide a manager for this model
        so Django knows how to create and control users
        using the Django command line tool"""
    objects = UserProfileManager()

    """This overrides Django username to use email"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """Functions below are standard to return user's Name
        for this model. Used by Django"""
    def get_full_name(self):
        """Retrieve Full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return models as a string"""
        return self.status_text
