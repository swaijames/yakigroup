from django.contrib import admin
from websiteapi import models


# Register your models here.

class Admin_Dash(admin.AdminSite):
    site_header = 'Yakigroup Admin Login'


yakigroup_site = Admin_Dash(name='YakiGroupAdmin')

yakigroup_site.register(models.Destination)
yakigroup_site.register(models.Destination_Detail)
yakigroup_site.register(models.Package)
yakigroup_site.register(models.Package_Details)
yakigroup_site.register(models.Hero)
yakigroup_site.register(models.Gallery)
