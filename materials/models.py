from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Material(models.Model):
    class Meta:
        db_table = "Materials"

    def __str__(self):
        return self.title

    # type_choises = (
    #    (1, "workshop"),
    #    (2, "helpful article"),
    # )
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images')
    description = models.CharField(blank=True, max_length= 200)
    # full_discription = models.TextField(blank=True)
    # type = models.CharField(choices=type_choises, max_length=10)
    attach = models.FileField(upload_to='files')
    date = models.DateTimeField(default=timezone.now)

    def get_download_url(self):
        return "/materials/download/%s" % self.attach


class Event(models.Model):
    class Meta:
        db_table = "Events"
        ordering = ['when']

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    when = models.DateTimeField('date of event')
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return "/event/%i/" % self.id

    def get_image(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url
        else:
            return u'<p>Something wrong with this image</p>'

    get_image.allow_tags = True


class Workshops(models.Model):
    class Meta:
        db_table = "Workshops"
        ordering = ['timestamp']
        verbose_name_plural = "Workshops"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)

    def get_image(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url
        else:
            return u'<p>Image not found</p>'

    get_image.allow_tags = True
