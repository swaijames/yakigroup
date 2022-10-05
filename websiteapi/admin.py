from django.contrib import admin
from .models import *


class YakiGroupAdmin(admin.AdminSite):
    site_header = 'YakiGroup Admin '


yakigroup_site = YakiGroupAdmin(name='YakiGroupAdmin')

# Register your models here.
yakigroup_site.register(Package)
yakigroup_site.register(Package_Details)
yakigroup_site.register(Destination)
yakigroup_site.register(Destination_Detail)
yakigroup_site.register(Gallery)
yakigroup_site.register(Hero)
