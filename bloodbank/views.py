from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import regUser

# Create your views here.

def index(request):
    return redirect("login")

def home(request):
    return render(request,"home.html")

def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['name']
        blood = request.POST['blood']
        dob = request.POST['dob']
        email = request.POST['email']
        contact = request.POST['contact']

        if (regUser.objects.filter(first_name=first_name).exists()):
                messages.info(request,'Person already registered')
                return redirect('register')
        else:
            reg_user = regUser.objects.create(
                first_name = first_name,
                email = email,
                blood = blood,
                dob = dob,
                contact = contact,
            )
            reg_user.save()
            return redirect('home')
    else:
        return render(request,'register.html')

def display(request):
    reg_users = regUser.objects.all()
    return render(request,'display.html',{"reg_users": reg_users})