from django.contrib import admin
from base.models import Banners, Areas

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ('index', 'image', 'url')

    ordering = ('index',)

    list_per_page = 50


class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aTitle', 'parent')

    search_fields = ('aTitle',)

    ordering = ('id',)

    list_per_page = 50


admin.site.register(Banners, BannerAdmin)
admin.site.register(Areas, AreaInfoAdmin)
