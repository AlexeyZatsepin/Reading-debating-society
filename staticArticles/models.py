from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class Flatblock(models.Model):
    class Meta:
        db_table = 'Flatblocks'

    title = models.CharField(max_length=50, help_text="don't delete it")
    content = models.TextField(help_text=u'p is paragraph tag, h2 is title tag, u can use it if you want')

    def __str__(self):
        return self.title


class FlatAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {"fields": ("title",)}),
        ("Content Warning: using js scripts in content is very dangerous", {"fields": ("content",)}),
    ]


admin.site.register(Flatblock,FlatAdmin)
