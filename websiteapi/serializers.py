from rest_framework import serializers
from website.models import *
from tourmanager.models import *


class WebsiteContectsSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebsiteContects
        fields = "__all__"


class TourRegionsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = "__all__"


class TourDestinationsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = "__all__"


class TourSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = "__all__"


class TourDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourData
        fields = "__all__"
