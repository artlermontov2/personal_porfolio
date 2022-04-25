from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def home(request):
    projects = Project.objects.all()  # Импортируем все записи о проектах из БД
    return render(request, 'portfolio/home.html', {'projects': projects})
