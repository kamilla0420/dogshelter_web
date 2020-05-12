"""
Definition of models.
"""

from django.db import models
from django.shortcuts import get_object_or_404
import datetime

year_dropdown = []
year_dropdown.append(('ismeretlen', 'Ismeretlen'))
for y in range((datetime.datetime.now().year - 15), (datetime.datetime.now().year + 1)):
    year_dropdown.append((y, y))

# class Meta:
#         db_table = 'Kutyák'

class Dog(models.Model):
    adopted_choices = [
        ('adopted', 'Igen'),
        ('adoptable', 'Nem'),
    ]

    name = models.CharField(max_length=150, verbose_name="Név")
    breed = models.CharField(max_length=150, default='Keverék', verbose_name="Fajta")
    birth_year = models.IntegerField(choices=year_dropdown, verbose_name="Születési év")
    body = models.TextField(verbose_name="Leírás")
    adopted = models.CharField(
        max_length=15,
        choices=adopted_choices,
        default='adoptable',
        verbose_name="Örökbeadott?"
    )
    income_date = models.DateField(verbose_name="Felvételi dátum")
    
    class Meta:
    #     db_table = 'Kutyák'
      verbose_name_plural = 'Kutyák'
    
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
    image = models.ImageField(upload_to='images/', verbose_name="Képek")

    class Meta:
        verbose_name_plural = 'Képek a kutyáról'