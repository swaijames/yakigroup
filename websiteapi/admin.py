from django.contrib import admin
from .models import *

# class YakiGroupAdmin(admin.AdminSite):
#     site_header = 'YakiGroup Admin '
#
#
# yakigroup_site = YakiGroupAdmin(name='YakiGroupAdmin')

# Register your models here.
admin.site.register(Package)
admin.site.register(Package_Details)
admin.site.register(Destination)
# admin.site.register(Destination_Detail)
admin.site.register(Gallery)
admin.site.register(Hero)
admin.site.register(Profile)
