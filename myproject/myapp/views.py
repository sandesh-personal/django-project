from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse("<h1> this is from views.py<h1/>")

def root_view_page(request):
    return render(request, template_name= "myapp/root_page.html")

def portfolio(request):
    return render(request, template_name= "portfolio/index.html")