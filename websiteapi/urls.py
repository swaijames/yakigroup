from django.urls import path, include
from .router import router
from . import views

urlpatterns = [

    path('api', include(router.urls)),
    path('booking', views.booking, name='booking'),
    path('booking_add', views.booking_add, name='booking_add'),
    path('booking_edit', views.booking_edit, name='booking_edit'),
    path('customer', views.customer, name='customer'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('reset', views.reset, name='reset'),
]
