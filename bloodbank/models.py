from django.db import models

# Create your models here.

class RegUser(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=20)
    blood = models.CharField(max_length=4)
    email = models.CharField(max_length=25)
    contact = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)