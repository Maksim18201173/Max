# main/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),  # или views.home, если хотите назвать home
    path('smartphones/', views.smartphones, name='smartphones'),
    path('laptops/', views.laptops, name='laptops'),
    path('tv/', views.tv, name='tv'),
    path('audio/', views.audio, name='audio'),
]