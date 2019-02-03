from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture, Category

def baby(request):
    picture_list = Picture.objects.all().order_by('-created_time')
    return render(request, 'baby/index.html', context={'picture_list': picture_list})

def index(request):
    return render(request, 'homepage.html')

def autodetail(request):
    return render(request, 'baby/babyauto.html')