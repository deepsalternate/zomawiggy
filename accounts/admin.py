from django.contrib import admin
from .models import User,userprofile
from django.contrib.auth.admin import UserAdmin 

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=('email','username','first_name','last_name','is_active','role')
    ordering=('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User,CustomUserAdmin)
admin.site.register(userprofile)

