from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Gallery, News, Story

def contact(request):
    return render(request, 'general/contact.html')

def gallery(request):
    gallery = Gallery.objects
    return render(request, 'general/gallery.html',{'gallery':gallery})

def news(request):
    news = News.objects.order_by('-pub_date')
    return render(request, 'general/news.html',{'news':news})

def stories(request):
    stories = Story.objects.order_by('-pub_date')
    return render(request, 'general/stories.html',{'stories':stories})