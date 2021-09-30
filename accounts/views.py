from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.

def signup(request):
    if (request.method == 'POST'):
        User = get_user_model()
        password1 = request.POST['pass']
        password2 = request.POST['conpass']
        if (password1 == password2):
            dpimg = request.POST['profile_photo']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            dob = request.POST['dob']
            contact = request.POST['contact']
            email = request.POST['email']
            password = password1
            print (dpimg)

            if (User.objects.filter(email=email).exists()):
                messages.info(request,'User with email exists')
                print ("Email already present in DB")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    dpimg = dpimg,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    dob = dob,
                    contact = contact,
                    password = password,
                    haveimg = False
                )
                user.save()
                print ("New user created!")
                return redirect('login')
        else:
            messages.info(request,'Passwords does not match')
            print ("pass error!")
            return redirect('signup')
    else:
        return render(request,'signup.html')

def login(request):
    if (request.method == 'POST'):
        username = request.POST['email']
        password = request.POST['pass']
        user = auth.authenticate(
            username = username,
            password = password
        )
        if (user is not None):
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials!')
            print ("Invalid credentials!")
            return redirect('login_page')
    else:
        return render(request,'login.html')

def logout(request):
    print ("logout")
    auth.logout(request)
    return redirect("login")