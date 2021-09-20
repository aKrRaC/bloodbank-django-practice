from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):

    #performing addition
    num1 = request.GET['n1']
    num2 = request.GET['n2']
    result = int(num1) + int(num2)


    return render(request,'result.html',{'result':result, 'num1':num1, 'num2':num2})