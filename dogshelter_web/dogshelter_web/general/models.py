from django.db import models
from django.contrib.auth.models import User

class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y. %b.')

class News(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    heading = models.TextField(null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y. %b. %e.')

    def small_summary(self):
        return self.body[:100]

    def summary(self):
        return self.body[:200]

class Story(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%Y. %b. %e.')