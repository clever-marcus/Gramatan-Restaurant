from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def index(request):
    context = {}
    return render(request, 'burger/index.html', context)

def speciality(request):
    context = {}
    return render(request, 'burger/speciality.html', context)

def popular(request):
    popular_food = Popular.objects.all()
    context = {'popular_food': popular_food}
    return render(request, 'burger/popular.html', context)

def gallery(request):
    gallery_food = Gallery.objects.all()
    context = {'gallery_food': gallery_food}
    return render(request, 'burger/gallery.html', context)

def review(request):
    context = {}
    return render(request, 'burger/review.html', context)

def checkout(request):
    context = {}
    return render(request, 'burger/checkout.html', context)

def order(request):
    context = {}
    return render(request, 'burger/order.html', context)