from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'middle_name', 'role', 'group', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'group')
    search_fields = ('username', 'last_name', 'first_name', 'email')

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('middle_name', 'phone', 'group', 'role')}),
    )