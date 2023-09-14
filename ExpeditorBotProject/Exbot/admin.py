from django.contrib import admin
from .models import User, Point


@admin.register(User) 
class UserConfig(admin.ModelAdmin):
    pass


@admin.register(Point) 
class PointConfig(admin.ModelAdmin):
    pass
