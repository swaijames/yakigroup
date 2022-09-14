from django.db import models
from django.contrib.auth.models import User
from pkg_resources import _


class WebsiteContects(models.Model):
    websection = models.CharField(max_length=255, blank=True)
    heading1 = models.CharField(max_length=255, blank=True)
    heading2 = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    attachment_image = models.ImageField(upload_to='website/images', blank=True)
    attachment_file = models.FileField(upload_to='website/uploads', blank=True)
    datafeatured = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "websiteContent"
        verbose_name_plural = "websiteContents"


class HomeBanner(models.Model):
    image = models.FileField(blank=True)
