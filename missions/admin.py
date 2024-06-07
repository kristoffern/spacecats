from django.contrib import admin
from .models import SpaceCat, Mission

@admin.register(SpaceCat)
class SpaceCatAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'age', 'mission_count')
    search_fields = ('name', 'role')

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'launch_date')
    search_fields = ('name',)
    filter_horizontal = ('spacecats',)
