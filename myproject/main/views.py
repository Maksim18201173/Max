# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def index(request):
    return render(request, 'main/index.html')

# Добавьте функции для ваших страниц
def smartphones(request):
    return render(request, 'main/smartphones.html')

def laptops(request):
    return render(request, 'main/laptops.html')

def tv(request):
    return render(request, 'main/tv.html')

def audio(request):
    return render(request, 'main/audio.html')