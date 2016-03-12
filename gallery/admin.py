from django.contrib import admin
from .models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'year', 'title')
    list_filter = ['year']
    search_fields = ['title']
    ordering = ['year']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'album_id')
    list_filter = ('album_id__title','title')
    search_fields = ['album_id__title','title']
    ordering = ['album_id']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
