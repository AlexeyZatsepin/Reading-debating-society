# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Sponsor(models.Model):
    class Meta():
        db_table = "Sponsors"

    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')
    link = models.URLField(help_text='sponsors link, url like : http://google.com')
    description = models.TextField()

    def get_link(self):
        return self.link

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url
        else:
            return u'<p>Something wrong with this image</p>'

    get_image.allow_tags = True


class Slider(models.Model):
    class Meta():
        db_table = "Slider"
        verbose_name = "photo"
        verbose_name_plural = 'Slides'

    def __str__(self):
        return self.image.name

    image = models.ImageField(help_text="photos size must be 1280 × 720 ", upload_to='images')

    def get_image(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url
        else:
            return u'<p>Something wrong with this image</p>'

    get_image.short_description = 'All slides'
    get_image.allow_tags = True


class Visits(models.Model):
    class Meta():
        db_table = "Visit"
        verbose_name = "Visit"
        verbose_name_plural = "Visits"
        app_label = 'app'

    # page_choices={}

    def __str__(self):
        return self.datetime.__str__()

    datetime = models.DateTimeField(default=timezone.now)

    def get_time(self):
        return self.datetime
        # page = models.CharField(max_length=10, choices=page_choices)
