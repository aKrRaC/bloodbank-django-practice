from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField
    dpimp = models.ImageField(upload_to='assets/images')
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    blood = models.CharField(max_length=4)
    email = models.CharField(max_length=25)
    contact = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    haveimg = models.BooleanField(default=False)