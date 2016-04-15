from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Album, Photo


class AlbumAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_display = ('get_image', 'year', 'title')
    list_filter = ['year']
    search_fields = ['title']
    ordering = ['year']
    fieldsets = [
        ("Title", {"fields": ("title",)}),
        ("Overall", {"fields": ("cover", "year")}),
    ]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'album_id')
    list_filter = ('album_id__title','title')
    search_fields = ['album_id__title','title']
    ordering = ['album_id']
    fieldsets = [
        ("Overall", {"fields": ("title", "album_id", "photo")}),
        ("Help text", {"fields": ("description",)}),
    ]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
