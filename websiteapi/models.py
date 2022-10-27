from datetime import datetime, time
from datetime import datetime, date

from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import uuid

STATUS_CHOICE = (
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('blocked', 'blocked'),

)


class Package(models.Model):
    package_title = models.CharField(max_length=200, blank=False, null=False, default="")
    package_price = models.IntegerField(default=000000)
    package_duration = models.CharField(max_length=200, blank=False, null=False, default="")
    package_tour_type = models.CharField(max_length=200, blank=False, null=False, default="")
    package_tour_guide = models.CharField(max_length=200, blank=False, null=False, default="")
    package_people_group = models.CharField(max_length=200, blank=False, null=False, default="")
    package_status = models.CharField(max_length=200, blank=False, null=False, default="")
    description = models.TextField(blank=True, default="none")
    info_detail = models.TextField(blank=True, default="none")
    info_image1 = models.FileField(blank=False, default=None)
    info_image2 = models.FileField(blank=False, default=None)
    info_video = models.FileField(blank=True)
    info_destination = models.CharField(max_length=200, blank=False, default="")
    info_depature_time = models.DateField(default=date.today())
    info_return_time = models.DateField(default=date.today())
    info_depature = models.CharField(max_length=200, blank=False, default="")
    info_included1 = models.CharField(max_length=200, default="none")
    info_included2 = models.CharField(max_length=200, default="none")
    info_included3 = models.CharField(max_length=200, default="")
    info_included4 = models.CharField(max_length=200, default="")
    info_included5 = models.CharField(max_length=200, default="")
    info_excluded1 = models.CharField(max_length=200, default="")
    info_excluded2 = models.CharField(max_length=200, default="")
    info_excluded3 = models.CharField(max_length=200, default="")
    info_excluded4 = models.CharField(max_length=200, default="")
    info_excluded5 = models.CharField(max_length=200, default="")
    travel_status = models.CharField(max_length=200, default="")
    travel_plan_detail = models.TextField(blank=False, default="")
    travel_plan_day_title = models.CharField(max_length=200, blank=False, default="")
    travel_plan_day_time_From = models.CharField(default="10:00", max_length=200)
    travel_plan_day_time_To = models.CharField(default="10:00", max_length=200)
    travel_plan_day_description_To = models.TextField(blank=False, default="")
    #
    travel_plan2_detail = models.TextField(blank=False, default="")
    travel_plan2_day_title = models.CharField(max_length=200, blank=False, default="")
    travel_plan2_day_time_From = models.CharField(default="10:00", max_length=200)
    travel_plan2_day_time_To = models.CharField(default="10:00", max_length=200)
    travel_plan2_day_description_To = models.TextField(blank=False, default="")
    #
    travel_plan3_detail = models.TextField(blank=False, default="")
    travel_plan3_day_title = models.CharField(max_length=200, blank=False, default="")
    travel_plan3_day_time_From = models.CharField(default="10:00", max_length=200)
    travel_plan3_day_time_To = models.CharField(default="10:00", max_length=200)
    travel_plan3_day_description_To = models.TextField(blank=False, default="")
    #
    travel_plan4_detail = models.TextField(blank=False, default="")
    travel_plan4_day_title = models.CharField(max_length=200, blank=False, default="")
    travel_plan4_day_time_From = models.CharField(default="10:00", max_length=200)
    travel_plan4_day_time_To = models.CharField(default="10:00", max_length=200)
    travel_plan4_day_description_To = models.TextField(blank=False, default="")
    #
    travel_plan5_detail = models.TextField(blank=False, default="")
    travel_plan5_day_title = models.CharField(max_length=200, blank=False, default="")
    travel_plan5_day_time_From = models.CharField(default="10:00", max_length=200)
    travel_plan5_day_time_To = models.CharField(default="10:00", max_length=200)
    travel_plan5_day_description_To = models.TextField(blank=False, default="")
    #
    tour_gallery_image1 = models.FileField(default=None)
    tour_gallery_image2 = models.FileField(default=None)
    tour_gallery_image3 = models.FileField(default=None, blank=False)
    tour_gallery_image4 = models.FileField(default=None, blank=False)
    tour_gallery_image5 = models.FileField(default=None, blank=False)
    map_latitude = models.CharField(max_length=255, blank=True)
    map_longtude = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=datetime.today())
    updated_at = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.package_title


# class Package_Details(models.Model):
#     package = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True)
#     description = models.TextField(blank=False, default="")
#     info_detail = models.TextField(blank=False)
#     info_image1 = models.FileField(blank=False)
#     info_image2 = models.FileField(blank=False)
#     info_video = models.FileField(blank=True)
#     info_destination = models.CharField(max_length=200, blank=False)
#     info_depature_time = models.DateField(default=date.today())
#     info_return_time = models.DateField(default=date.today())
#     info_depature = models.CharField(max_length=200, blank=False)
#     info_included1 = models.CharField(max_length=200)
#     info_included2 = models.CharField(max_length=200)
#     info_included3 = models.CharField(max_length=200)
#     info_included4 = models.CharField(max_length=200)
#     info_included5 = models.CharField(max_length=200)
#     info_excluded1 = models.CharField(max_length=200)
#     info_excluded2 = models.CharField(max_length=200)
#     info_excluded3 = models.CharField(max_length=200)
#     info_excluded4 = models.CharField(max_length=200)
#     info_excluded5 = models.CharField(max_length=200)
#     travel_status = models.CharField(max_length=200)
#     travel_plan_detail = models.TextField(blank=False)
#     travel_plan_day_title = models.CharField(max_length=200, blank=False)
#     travel_plan_day_time_From = models.CharField(default="10:00", max_length=200)
#     travel_plan_day_time_To = models.CharField(default="10:00", max_length=200)
#     travel_plan_day_description_To = models.TextField(blank=False)
#     tour_gallery_image1 = models.FileField(default=None, blank=False)
#     tour_gallery_image2 = models.FileField(default=None, blank=False)
#     tour_gallery_image3 = models.FileField(default=None, blank=False)
#     tour_gallery_image4 = models.FileField(default=None, blank=False)
#     tour_gallery_image5 = models.FileField(default=None, blank=False)
#     map_latitude = models.CharField(max_length=255, blank=True)
#     map_longtude = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = "Package_Detail"
#         verbose_name_plural = "Packages_Details"
#
#     def __str__(self):
#         return self.package


class Destination(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.FileField(blank=False)
    sub_image1 = models.FileField(blank=True)
    sub_image2 = models.FileField(blank=True)
    departureTime = models.DateField(default=date.today())
    return_time = models.DateField(default=date.today())
    map_latitude = models.CharField(max_length=255, blank=True)
    map_longtude = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=False)
    departure = models.CharField(max_length=255, blank=False)
    status = models.CharField(choices=STATUS_CHOICE, blank=False, null=False, max_length=255, default='active')
    created_at = models.DateTimeField(default=datetime.today())
    updated_at = models.DateTimeField(default=datetime.today())

    # class Meta:
    #     verbose_name = "Destination"
    #     verbose_name_plural = "Destinations"
    #
    # def __str__(self):
    #     return self.title


# class Destination_Detail(models.Model):
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     details = models.TextField(blank=False)
#     title = models.CharField(max_length=255, blank=False)
#     image1 = models.FileField(blank=False)
#     image2 = models.FileField(blank=False)
#     departure = models.CharField(max_length=255, blank=False)
#     departure_time = models.DateTimeField(auto_now_add=True)
#     return_time = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = "Destination_Detail"
#         verbose_name_plural = "Destinations_Details"
#
#     def __str__(self):
#         return self.destination


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


class Booking(models.Model):
    fullname = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    phone = models.IntegerField(blank=False, null=True)
    ticket_type = models.CharField(max_length=255, blank=False)
    adult = models.IntegerField(blank=False, null=True)
    child = models.IntegerField(blank=False, null=True)
    message = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.fullname
