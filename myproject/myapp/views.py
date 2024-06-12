from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse("<h1> this is from views.py<h1/>")

def root_view_page(request):
    return render(request, template_name= "myapp/root_page.html")

def portfolio(request):
    return render(request, template_name= "portfolio/index.html")

def home(request):
    return render(request, template_name= "portfolio/index.html")

def learning_dtl_view(request):
    c = {"name": "Prixa Academy", "student": "jane"}
    s = [
        {"name": "jon", "age":30, "display": True},
        {"name": "jon cena", "age":30, "display": False},
        {"name": "jon abharm", "age": 30, "display": True},
        {"name": "jonny ", "age": 30, "display": True},
    ]
    c.update(students=s)
    return render(request, template_name= "myapp/dtl.html", context=c )




# featurs from DTTL
# 1. {% laod static %}
# 2. {% url, "home" %}
# 3. {% sattic "static/path %}
# 4. {{name}}


def using_bootstrap_view(request):
    s =[
        {"name": "jon", "age":30, "email": "aa@gmail.com", "address": "ktm", "display": True},
        {"name": "jon cena", "age":30, "email": "aa@gmail.com", "address": "ktm", "display": False},
        {"name": "jon abharm", "age": 30, "email": "aa@gmail.com", "address": "ktm", "display": True},
        {"name": "jonny ", "age": 30, "email": "aa@gmail.com", "address": "ktm", "display": True},
    ]
    return render(request, template_name= "myapp/using_bootstrap.html", context= {"students": s})