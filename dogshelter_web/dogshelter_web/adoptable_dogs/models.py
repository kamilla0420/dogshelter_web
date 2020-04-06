"""
Definition of models.
"""

from django.db import models
from django.shortcuts import get_object_or_404
import datetime

year_dropdown = []
for y in range((datetime.datetime.now().year - 20), (datetime.datetime.now().year)):
    year_dropdown.append((y, y))

class Dog(models.Model):
    name = models.CharField(max_length=150)
    breed = models.CharField(max_length=150, default='Keverek')
    income_date = models.DateField()
    birth_year = models.IntegerField(choices=year_dropdown)
    body = models.TextField()

    #For printing
    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:100]

    def income_date_pretty(self):
        return self.income_date.strftime('%Y. %b. %e.')

    def get_first_image(self):
        return self.dogimages_set.all()[0]

class DogImages(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')