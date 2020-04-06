from django.shortcuts import render
from .models import AdoptedDog

def adopted_dogs(request):
    dogs = AdoptedDog.objects
    return render(request, 'adopted_dogs/adopted_dogs.html',{'dogs':dogs})