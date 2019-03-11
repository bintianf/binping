import markdown
from markdown.extensions.toc import TocExtension
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.text import slugify

from .models import Picture, Age, Group

def babyindex(request):
    recent_group = Group.objects.latest('created_time')
    cur_age = Group.objects.latest('created_time').age
    group_list = Group.objects.filter(age = cur_age)
    pic_list = Picture.objects.filter(group=recent_group.id)
    return render(request, 'baby/index.html', context={'pic_list': pic_list, 'recent_group': recent_group, 'cur_age': cur_age, 'group_list': group_list})

def age(request, pk):
    cur_age = get_object_or_404(Age, pk=pk)
    recent_group = Group.objects.filter(age = cur_age).latest('created_time')
    group_list = Group.objects.filter(age = cur_age)
    pic_list = Picture.objects.filter(group=recent_group.id)
    return render(request, 'baby/babydetail.html', context={'pic_list': pic_list, 'recent_group': recent_group, 'cur_age': cur_age, 'group_list': group_list})

def group(request, pk):
    recent_group = get_object_or_404(Group, pk=pk)
    cur_age = recent_group.age
    group_list = Group.objects.filter(age = cur_age)
    pic_list = Picture.objects.filter(group=recent_group.id)
    return render(request, 'baby/babydetail.html', context={'pic_list': pic_list, 'recent_group': recent_group, 'cur_age': cur_age, 'group_list': group_list})