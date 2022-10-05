from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView


# # Create your views here.
# class AuthView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class PackageView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Package.objects.all()
    serializer_class = PackageSerialiser


class Package_Detail_View(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin

):
    queryset = Package_Details.objects.all()
    serializer_class = Package_Detail_Serialiser


class DestnationView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerialiser


class Destination_Detail_View(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Destination_Detail.objects.all()
    serializer_class = Destination_Detail_Serialiser


class GalleryView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class HeroView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


def index(request):
    return render(request, 'Tour/index.html')


# Create your views here.
def booking(request):
    return render(request, 'Tour/bookings.html')


def booking_add(request):
    return render(request, 'Tour/booking-add.html')


def booking_edit(request):
    return render(request, 'Tour/booking-edit.html')


def customer(request):
    return render(request, 'Tour/customers.html')


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('/dashboard/')

            messages.info(request, ' Invalid password')
            return redirect('/')
        return render(request, 'auths/login.html')
    except Exception as e:
        print(e)
