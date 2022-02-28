from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.order_by('-id')[:3]
    return render(request, 'portfolio/home.html', {'projects': projects})
