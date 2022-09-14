from django.http import HttpResponse
from django.shortcuts import render
from tourmanager.models import Destinations
from .models import WebsiteContects


def home(request):
    slider = WebsiteContects.objects.all().filter(websection='slider')
    slider = {'sliders': slider}
    return render(request, 'home.html', slider)


def contact(request):
    return render(request, 'contactus.html')


def about(request):
    return render(request, 'about.html')


def tours(request):
    return  render(request, 'tours.html')


def destinations(request):
    destination_list = Destinations.objects.all()
    destination_list = {'destinations': destination_list}
    return render(request, 'destinations.html', destination_list)