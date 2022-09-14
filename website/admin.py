from django.contrib import admin
from website.models import *


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('websection', 'heading1', 'heading2')


admin.site.register(WebsiteContects, WebsiteAdmin)
admin.site.register(HomeBanner)