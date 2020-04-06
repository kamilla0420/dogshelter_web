"""
Definition of views.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Dog

def home(request):
    dogs = Dog.objects
    return render(request, 'adoptable_dogs/home.html',{'dogs':dogs})

def detail(request, dog_id, dog_name):
    detailed_dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'adoptable_dogs/dog_in_details.html',{'dog':detailed_dog})
