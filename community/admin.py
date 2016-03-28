from django.contrib import admin
from models import Committee,Committee_stuff,Alumni


class StuffAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name')


admin.site.register(Committee_stuff, StuffAdmin)
admin.site.register(Committee)
admin.site.register(Alumni)