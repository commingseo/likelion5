from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs= Blog.objects.all
    return render(request, "home.html", {"blogs": blogs})


def new(request):
    return render(request, "new.html")

def create(request):
# 여기서 글을 DB에 저장
    title = request.GET["title"]
    body = request.GET["body"]
    blog = Blog()
    blog.title = title
    blog.body = body
    blog.time = timezone.now()
    blog.save()
    return redirect('home')
