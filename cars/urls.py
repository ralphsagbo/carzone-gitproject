"""carzone/pages URL Configuration
phil_2: when you create a pages, you lust include an urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
]
