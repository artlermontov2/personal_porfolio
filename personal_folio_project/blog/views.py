from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blogs


def all_blogs(request):
    blogs = Blogs.objects.order_by('-date')[:5] 
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)  # Пытается найти объект под нужным номером, и если не находит, но выбаст ошибку 404
    return render(request, 'blog/detail.html', {'blog': blog})