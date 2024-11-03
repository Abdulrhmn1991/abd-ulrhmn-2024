# main/admin.py
from django.contrib import admin
from .models import DailyFlyer, Page

@admin.register(DailyFlyer)
class DailyFlyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    search_fields = ('description',)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'working_hours', 'whatsapp_number')
    list_filter = ('area',)
    search_fields = ('title', 'description')
