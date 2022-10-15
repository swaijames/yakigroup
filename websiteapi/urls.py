from django.urls import path, include
from .router import router
from . import views
from .views import DestinationDelete

urlpatterns = [

    path('', include(router.urls)),
    path('booking', views.booking, name='booking'),
    path('booking_add', views.booking_add, name='booking_add'),
    path('booking_edit', views.booking_edit, name='booking_edit'),
    path('customer', views.customer, name='customer'),
    path('yaki_dashboard', views.index, name='index'),
    path('login', views.admin_login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('profile', views.profile, name='profile'),
    path('room_list', views.room_list, name='room_list'),
    path('destnation_delete/<pk>', DestinationDelete.as_view(), name='destination_delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update_destination/<int:id>', views.update_destination, name='update_destination'),
    path('room_type', views.room_type, name='room_type'),
    path('destination_add', views.destination_add, name='destination_add'),

    path('package_list', views.package_list, name='package_list'),
    path('package_add', views.package_add, name='package_add'),

<<<<<<< HEAD



=======
>>>>>>> e7a40edd419e50affa8417c865bd9ff6d1a53044
    path('password_reset_confirm/<slug:uid>/', views.change_password, name='password_reset_confirm'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('reset', views.reset, name='reset'),
]
