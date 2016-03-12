from django.contrib import admin
from .models import Material,Event

class EventManager(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'when')
    list_filter = ['when']
    search_fields = ['title']
    ordering = ['when']


admin.site.register(Event, EventManager)
admin.site.register(Material)