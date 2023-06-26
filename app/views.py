from django.shortcuts import render
from django.http import request
from .models import About, Service, Portfolio, Blog, Education


def index(request):
    return render(request,"index.html")

def about(request):
    refferances = About.objects.all()
    educations = Education.objects.all()
    
    return render(request,'about.html',{'refferances':refferances,'educations':educations})

def services(request):
    service = Service.objects.all()
    return render(request,'services.html',{'services':service})

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request,'portfolio.html',{'portfolios':portfolios})

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')