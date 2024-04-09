from django.shortcuts import render
from django.template.loader import get_template
#from .models import Player

def homepage_view(request):
    return render(request, 'mysite/homepage.html')

def submit(request):
    return None