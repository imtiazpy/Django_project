from django.contrib import admin
from .models import Profile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User',         {'fields': ['user']}),
        ('Image', {'fields': ['image']}),
        
    ]



admin.site.register(Profile, ProfileAdmin)
