from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:dog_id>/<str:dog_name>', views.detail, name='detail'),
]
