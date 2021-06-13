from django.urls import path, include

from . import views

urlpatterns = [
    path('api/v1/search/', views.django_xchange, name='djangoXchange'),
]
