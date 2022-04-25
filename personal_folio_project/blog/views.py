from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs


def all_blogs(request):
    blogs = Blogs.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
