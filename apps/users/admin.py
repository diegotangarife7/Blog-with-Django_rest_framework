from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'last_name', 'gender', 'twitter', 'avatar', 'is_active', 'is_staff']

admin.site.register(User, UserAdmin)