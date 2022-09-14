from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('tours', views.tours, name='tours'),
    path('destinations', views.destinations, name='destinations')
]
