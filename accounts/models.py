from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .manager import User_manager

# Create your models here.
class User(AbstractUser):
    dpimg = models.ImageField(upload_to='assets/images')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    contact = models.CharField(max_length=200)
    dob = models.CharField(max_length=10)
    haveimg = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = [first_name, last_name, email, contact, dob, haveimg]
    USERNAME_FIELD = "email"
    objects = User_manager()

