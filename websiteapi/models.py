from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import uuid


class Package(models.Model):
    package_title = models.CharField(max_length=200, blank=False, null=False)
    package_price = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    package_duration = models.IntegerField(blank=False)
    package_tour_type = models.CharField(max_length=200, blank=False)
    package_tour_guide = models.IntegerField(blank=False)
    package_people_group = models.IntegerField(blank=False)

    def __str__(self):
        return self.package_title


class Package_Details(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, blank=False)
    info_detail = models.TextField(blank=False)
    info_image1 = models.FileField(blank=False)
    info_image2 = models.FileField(blank=False)
    info_video = models.FileField(blank=False)
    info_destination = models.CharField(max_length=200, blank=False)
    info_depature_time = models.DateTimeField(auto_now_add=True)
    info_return_time = models.DateTimeField(auto_now_add=True)
    info_depature = models.CharField(max_length=200, blank=False)
    info_included1 = models.CharField(max_length=200)
    info_included2 = models.CharField(max_length=200)
    info_included3 = models.CharField(max_length=200)
    info_included4 = models.CharField(max_length=200)
    info_included5 = models.CharField(max_length=200)
    info_excluded1 = models.CharField(max_length=200)
    info_excluded2 = models.CharField(max_length=200)
    info_excluded3 = models.CharField(max_length=200)
    info_excluded4 = models.CharField(max_length=200)
    info_excluded5 = models.CharField(max_length=200)
    travel_status = models.CharField(max_length=200)
    travel_plan_detail = models.TextField(blank=False)
    travel_plan_day_title = models.CharField(max_length=200, blank=False)
    travel_plan_day_time_From = models.DateTimeField(auto_now_add=True, blank=False)
    travel_plan_day_time_To = models.DateTimeField(auto_now=True, blank=False)
    travel_plan_day_description_To = models.TextField(blank=False)
    gallery_image = models.FileField(blank=False)
    map_latitude = models.CharField(max_length=255, blank=True)
    map_longtude = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Package_Detail"
        verbose_name_plural = "Packages_Details"

    def __str__(self):
        return self.package


class Destination(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.FileField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"

    def __str__(self):
        return self.title


class Destination_Detail(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    details = models.TextField(blank=False)
    title = models.CharField(max_length=255, blank=False)
    image1 = models.FileField(blank=False)
    image2 = models.FileField(blank=False)
    departure = models.CharField(max_length=255, blank=False)
    departure_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Destination_Detail"
        verbose_name_plural = "Destinations_Details"

    def __str__(self):
        return self.destination


class Gallery(models.Model):
    image = models.FileField(blank=False)
    video = models.FileField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.created_at


class Hero(models.Model):
    coursel_image1 = models.FileField(blank=False)
    coursel_image2 = models.FileField(blank=False)
    coursel_image3 = models.FileField(blank=False)
    title1 = models.CharField(max_length=255, blank=False)
    title2 = models.CharField(max_length=255, blank=False)
    title3 = models.CharField(max_length=255, blank=False)
    description1 = models.TextField(blank=False)
    description2 = models.TextField(blank=False)
    description3 = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"

    def __str__(self):
        return self.title1, self.title2, self.title3


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return '{}'.format(self.user)
