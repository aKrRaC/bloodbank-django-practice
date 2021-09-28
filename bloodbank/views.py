from django.shortcuts import render

# Create your views here.
reg_user_list = []
user_list = []

def index(request):
    return render(request,'index.html')

def signup_page(request):
    return render(request,'signup.html')

def signup(request):
    add_user = {}
    password1 = request.POST['pass']
    password2 = request.POST['conpass']
    if (password1 == password2):
        add_user['fname'] = request.POST['fname']
        add_user['lname'] = request.POST['lname']
        add_user['dob'] = request.POST['dob']
        add_user['contact'] = request.POST['contact']
        add_user['email'] = request.POST['email']
        add_user['pass'] = password1

        user_list.append(add_user)
        print (add_user)
        print (user_list)
        return render(request,'login.html')
    else:
        print ("pass error!")
        return render(request,'signup.html')

def login_page(request):
    return render(request,'login.html')

def login(request):
    login_user = []
    login_user.append(request.POST['email'])
    login_user.append(request.POST['pass'])
    for i in user_list:
        if (i["email"] == login_user[0] and i["pass"] == login_user[1]):
            return render(request,'home.html')
        else:
            return render(request,'login.html')

def home(request):
    login_status = request.session.get('login_status',1)
    if (login_status == 1):
        return render(request,'home.html')
    else:
        return render(request,'index.html')

def register_page(request):
    login_status = request.session.get('login_status',1)
    if (login_status == 1):
        return render(request,'register.html')
    else:
        return render(request,'index.html')

def register(request):
    reg_user = {}
    reg_user['name'] = request.POST['name']
    reg_user['blood'] = request.POST['blood']
    reg_user['dob'] = request.POST['dob']
    reg_user['email'] = request.POST['email']
    reg_user['contact'] = request.POST['contact']

    reg_user_list.append(reg_user)
    print(reg_user_list)
    return render(request,'display.html',{'userdet': reg_user_list})


def display(request):
    return render(request,'display.html',{'userdet': reg_user_list})