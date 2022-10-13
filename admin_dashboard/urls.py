from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking_add', views.booking_add, name='booking_add'),
    path('booking_edit', views.booking_edit, name='booking_edit'),
    path('customer', views.customer, name='customer')
]
