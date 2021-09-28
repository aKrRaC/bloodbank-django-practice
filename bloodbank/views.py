from django.shortcuts import render

# Create your views here.
reg_user_list = []

def index(request):

    return render(request,'index1.html')

def register(request):
    reg_user = {}
    reg_user['name'] = request.POST['name']
    reg_user['blood'] = request.POST['blood']
    reg_user['dob'] = request.POST['dob']
    reg_user['email'] = request.POST['email']
    reg_user['contact'] = request.POST['contact']

    reg_user_list.append(reg_user)
    print(reg_user_list)
    return render(request,'index1.html')

def display(request):
    return render(request,'display.html',{'userdet': reg_user_list})