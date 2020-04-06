from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y. %b. %e.')

class News(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y. %b. %e.')

class Story(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y. %b. %e.')