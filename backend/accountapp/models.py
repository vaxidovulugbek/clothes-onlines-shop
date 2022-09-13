import uuid

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    email = models.EmailField(max_length=200, unique=True)
    phoneNumber = models.CharField(max_length=13, unique=True, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return str(self.username)
