from django.contrib import admin
from .models import Material, Event, Workshops


class EventManager(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'when')
    list_filter = ['when']
    search_fields = ['title']
    ordering = ['when']
    fieldsets = [
        ("Event title", {"fields": ("title",)}),
        ("Date", {"fields": ("when",)}),
        ("About", {"fields": ("image", "description")}),
    ]


class WorkshopsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title')
    list_filter = ('timestamp',)
    search_fields = ['timestamp', 'title']
    ordering = ['-timestamp']
    exclude = ('timestamp',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    exclude = ('date',)
    fieldsets = [
        ("Overall", {"fields": ("title", "attach")}),
        ("Help text", {"fields": ("description",)}),
    ]

admin.site.register(Workshops, WorkshopsAdmin)
admin.site.register(Event, EventManager)
admin.site.register(Material, MaterialAdmin)
