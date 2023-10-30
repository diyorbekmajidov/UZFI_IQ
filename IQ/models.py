from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  password = models.CharField(max_length=128, blank=True, null=True)
  mobile_number = models.CharField(max_length=100, blank=True, null=True)
  username = models.CharField(max_length=150, unique=True, blank=True, null=True)
  is_active = models.BooleanField(default=True)

  class Meta:
      db_table = "my_user"

  def __str__(self):
      return self.mobile_number