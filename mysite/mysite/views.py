from django.shortcuts import render
from django.template.loader import get_template
#from .models import Player

def generator_view(request):
    template_name = 'mysite/homepage.html'
    try:
        template = get_template(template_name)
    except Exception as e:
        print(f"Error loading template '{template_name}': {e}")
    return render(request, template_name)

def submit(request):
    return None