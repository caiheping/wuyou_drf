from django.contrib import admin
from users.models import Users

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'area', 'avatar')

    list_per_page = 50


admin.site.register(Users, UsersAdmin)
