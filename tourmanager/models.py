from django.db import models
from django.contrib.auth.models import User
from pkg_resources import _


class Regions(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, blank=False)
    map_location = models.CharField(max_length=255, blank=True)
    region_featured_image = models.ImageField(upload_to='regions')

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Destinations(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    region = models.ForeignKey(Regions, on_delete=models.PROTECT)
    destination_name = models.CharField(max_length=30, blank=False)
    map_location = models.CharField(max_length=255, blank=True)
    destination_image = models.ImageField(upload_to='destinations')

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"


class DestnationTrip(models.Model):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE)
    travel_type = models.CharField(max_length=255, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)


class BookNow(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    travel_date = models.DateField(blank=False)
    Number_of_people = models.IntegerField(null=False, blank=False)


class Tours(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    tour_name = models.CharField(max_length=30, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    min_number_of_people = models.CharField(max_length=4, blank=False)
    max_number_of_people = models.CharField(max_length=4, blank=False)
    tour_price = models.FloatField(max_length=20, blank=False)

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"


class TourData(models.Model):
    tourid = models.ForeignKey(Tours, on_delete=models.PROTECT)
    region = models.ForeignKey(Regions, on_delete=models.PROTECT)
    destination = models.ForeignKey(Destinations, on_delete=models.PROTECT)
    number_of_days = models.CharField(max_length=3, blank=True)

    class Meta:
        verbose_name = "TourData"
        verbose_name_plural = "TourData"
