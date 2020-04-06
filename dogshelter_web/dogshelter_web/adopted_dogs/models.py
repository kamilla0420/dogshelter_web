"""
Definition of models.
"""

from django.db import models
from django.shortcuts import get_object_or_404
import datetime

year_dropdown = []
for y in range((datetime.datetime.now().year - 20), (datetime.datetime.now().year)):
    year_dropdown.append((y, y))

class AdoptedDog(models.Model):
    name = models.CharField(max_length=150)
    breed = models.CharField(max_length=150)
    adopt_date = models.DateField()
    birth_year = models.IntegerField()
    body = models.TextField()

    #For printing
    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:300]

    def adopt_date_pretty(self):
        return self.adopt_date.strftime('%Y. %b. %e.')