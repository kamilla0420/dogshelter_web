"""
Definition of views.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Dog

def home(request):
    adoptable_dogs = Dog.objects.filter(adopted="adoptable")
    return render(request, 'dogs/home.html',{'dogs':adoptable_dogs})

def detail(request, dog_id, dog_name):
    detailed_dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dogs/dog_in_details.html',{'dog':detailed_dog})

def adopted_dogs(request):
    adopted_dogs = Dog.objects.filter(adopted="adopted")
    return render(request, 'dogs/adopted_dogs.html',{'dogs':adopted_dogs})
