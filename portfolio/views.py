from django.shortcuts import render
from .models import Project

def home(request):
    # Traemos todos los registros de Project
    projects = Project.objects.all()    
    return render(request, 'home.html', {'projects':projects})
