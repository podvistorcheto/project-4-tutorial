from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manages the user accounts """

    def create_user(self, email, name, password=None):
        """to create new user profile"""
        if not email:
            raise ValueError('User must have and email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """to create superuser with specific details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ db model that stores the users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ retrieve the full name of user """
        return self.name

    def get_short_name(self):
        """ retrieve short name of user """
        return self.name

    def __str__(self):
        """ returns string representation of the user """
        return self.email