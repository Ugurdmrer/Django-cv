from django.shortcuts import render
from django.http import request
from .models import About, Service, Portfolio, Blog


def index(request):
    return render(request,"index.html")

def about(request):
    refferances = About.objects.all()
    
    return render(request,'about.html',{'refferances':refferances})

def services(request):
    return render(request,'services.html')

def portfolio(request):
    return render(request,'portfolio.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')