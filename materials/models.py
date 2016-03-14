from __future__ import unicode_literals

from django.db import models


class Material(models.Model):
    class Meta():
        db_table = "Materials"

    def __str__(self):
        return self.title

    #type_choises = (
    #    (1, "workshop"),
    #    (2, "helpful article"),
    #)
    title = models.CharField(max_length=60)
    #image = models.ImageField(upload_to='images')
    short_discription = models.TextField(blank=True)
    full_discription = models.TextField(blank=True)
    #type = models.CharField(choices=type_choises, max_length=10)
    attach = models.FileField(upload_to='materials')

    def get_absolute_url(self):
        return "/material/%i/" % self.id


class Event(models.Model):
    class Meta():
        db_table = "Events"
        ordering = ['when']

    def __str__(self):
        return self.title

    title = models.CharField(max_length=20)
    when = models.DateTimeField('date of event')
    image = models.ImageField(upload_to='images')
    short_discription = models.CharField(max_length=50)
    full_discription = models.TextField()

    def get_absolute_url(self):
        return "/event/%i/" % self.id

    def get_image(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url
        else:
            return u'<p>Something wrong with this image</p>'

    get_image.allow_tags = True
