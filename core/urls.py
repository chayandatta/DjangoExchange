from django.urls import path, include

from .views import django_xchange

urlpatterns = [
    path('api/v1/search/', django_xchange, name='djangoXchange'),
]
