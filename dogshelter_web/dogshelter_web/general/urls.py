from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('stories/', views.stories, name='stories'),
]
