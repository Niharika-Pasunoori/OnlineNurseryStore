from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Order
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets=[
        (
             None,
            {
            "fields":['username','password'],
            },
        ),

        (
            "Personal Info",
            {
                "fields":['first_name','last_name','email','phone','address'],
            }
        ),
       
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["is_active", "is_staff","is_superuser","groups","user_permissions"],
            },
        ),

        (
            "Important dates",
            {
                "fields":['date_joined','last_login'],
            }
        ),

        
    ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Order)