from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_staff']
    search_fields = ('username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    #ordering = ('username', )

admin.site.register(User, UserAdmin)

