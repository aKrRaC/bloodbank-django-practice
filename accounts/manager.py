from django.contrib.auth.models import BaseUserManager

#Create your manager here

class User_manager(BaseUserManager):
    def create_user(self, dpimg, first_name, last_name, email, contact, dob, haveimg, password):
        email = self.normalize_email(email)
        user = self.model(dpimg = dpimg, username = email, first_name = first_name, last_name = last_name, contact = contact, dob = dob, haveimg = haveimg, email=email, password = password)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, dpimg, first_name, last_name, email, contact, dob, haveimg, password):
        user = self.create_user(dpimg = dpimg, first_name = first_name, last_name = last_name, contact = contact, dob = dob, haveimg = haveimg, email=email, password = password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user