from abc import ABC

from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class PackageSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"


class Package_Detail_Serialiser(serializers.ModelSerializer):
    class Meta:
        model = Package_Details
        fields = "__all__"


class DestinationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"


class Destination_Detail_Serialiser(serializers.ModelSerializer):
    class Meta:
        model = Destination_Detail
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
