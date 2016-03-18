from __future__ import unicode_literals
from django.db import models


class Album(models.Model):
    class Meta():
        db_table = "Albums"

    year_choises = (
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/gallery/album/%i/" % self.id

    cover = models.ImageField(upload_to='images')
    year = models.CharField(max_length=10, choices=year_choises, default=2016)
    title = models.CharField(max_length=20, verbose_name= "album title")

    def get_image(self):
        if self.cover:
            return u'<img src="%s" width="100"/>' % self.cover.url
        else:
            return u'<p>Something wrong with this image</p>'

    get_image.short_description = 'All albums'
    get_image.allow_tags = True


class Photo(models.Model):
    class Meta():
        db_table = "Photos"

    def __str__(self):
        return self.title

    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="Album")
    photo = models.ImageField(upload_to='images',verbose_name="photo title", help_text="Photos in one album must have equal size!")
    title = models.TextField()
    discription = models.TextField(blank=True)

    def get_image(self):
        if self.photo:
            return u'<img src="%s" width="100"/>' % self.photo.url
        else:
            return u'<p>Something wrong with this image</p>'

    get_image.short_description = 'All albums'
    get_image.allow_tags = True