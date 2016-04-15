from django.contrib import admin
from .models import Committee, CommitteeMembers, Alumni


class StuffAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'position')
    list_filter = ('position',)
    fieldsets = [
        ("Name", {"fields": ("name",)}),
        ("Image", {"fields": ("image",)}),
        ("About", {"fields": ("position", "description")}),
        ("Committee", {"fields": ("committee",)}),
    ]


class AlumniAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields": ("first_name", "last_name")}),
        ("Image", {"fields": ("image",)}),
        ("Feedback", {"fields": ("email", "facebook", "linkedin")}),
        ("Info", {"fields": ("courses", "current_occupation", "time_in_society")}),
    ]
    list_display = ('first_name', 'last_name', 'email', 'time_in_society')
    list_filter = ('first_name', 'last_name', 'time_in_society')


admin.site.register(CommitteeMembers, StuffAdmin)
admin.site.register(Committee)
admin.site.register(Alumni, AlumniAdmin)
