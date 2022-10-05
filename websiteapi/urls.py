from django.urls import path, include
from .router import router
from . import views

urlpatterns = [

    path('', include(router.urls)),
    path('booking', views.booking, name='booking'),
    path('booking_add', views.booking_add, name='booking_add'),
    path('booking_edit', views.booking_edit, name='booking_edit'),
    path('customer', views.customer, name='customer'),
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
=======
    path('yaki_dashboard', views.index, name='index'),
    path('login', views.admin_login, name='login'),
    path('logout', views.logout_view, name='logout'),
>>>>>>> b49f882a000fb026f47f6d24fc4fda85edb536c3
    path('reset', views.reset, name='reset'),
]
