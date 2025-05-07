from django.shortcuts import render
from .models import authentication

# Create your views here.

def index(request): 
    return render(request , template_name='authentication/index.html') 
