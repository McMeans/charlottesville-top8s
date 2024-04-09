from django.shortcuts import render
#from .models import Player
from django.views import generic

class HomeView(generic.View):
    template_name = "home.html"

def generator_view(request):
    return render(request, 'home.html')

def submit(request):
    return None