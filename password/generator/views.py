from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'test password'})

def about(request):
    return render(request,'generator/about.html',{'about':'about data'})

def password(request):
    charaters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        charaters.extend(list('1234567890'))
    if request.GET.get('special'):
        charaters.extend(list('!@#$%^&*'))
    password=''
    for x in range(lenght):
        password += random.choice(charaters)
        #generate(password)
    return render(request,'generator/password.html',{'password':password})

def generate(request,password):
    return render(request,'generator/password.html',{'password':password})

    #print(password)
