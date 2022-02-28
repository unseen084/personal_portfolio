from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.order_by('-id')
    return render(request, 'portfolio/home.html', {'projects': projects})


def about_me(request):
    return render(request, 'portfolio/about_me.html')

