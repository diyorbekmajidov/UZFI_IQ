from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

# from apps.common.models import BaseModel
# from apps.users.managers import UserManager

# Create your models here.
class User(AbstractUser):
    sername = None
    first_name = models.CharField(_("first name"), max_length=255, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=255, null=True, blank=True)
    full_name = models.CharField(_("full name"), max_length=255)
    email = models.EmailField(_("email"), null=True, blank=True)
    phone_number = PhoneNumberField(_("phone number"), max_length=32, unique=True)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)
