from django.contrib import admin
from companys.models import Company, Job, Welfare

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'addr', 'area', 'personnel', 'company_start_time')

    ordering = ('id',)

    list_per_page = 50


class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'company', 'education', 'recruitment', 'city')

    search_fields = ('job',)

    ordering = ('id',)

    list_per_page = 50


class WelfareAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

    search_fields = ('name',)

    ordering = ('id',)

    list_per_page = 50


admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Welfare, WelfareAdmin)
