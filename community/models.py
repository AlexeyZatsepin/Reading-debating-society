from __future__ import unicode_literals

from django.db import models


class Committee(models.Model):
    class Meta():
        db_table = "Committee"

    def __str__(self):
        return self.time

    time = models.TextField('years',help_text="format: 2012-2013")
    image = models.ImageField(upload_to='images',blank=True)

    def get_absolute_url(self):
        return "/committee/%i/" % self.time


class Committee_stuff(models.Model):
    class Meta():
        db_table = "Stuff"
        verbose_name = "member"
        verbose_name_plural = "Stuff"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    discription = models.TextField(blank=True)
    image = models.ImageField(upload_to='images',blank=True)
    committee = models.ForeignKey(Committee)


class Alumni(models.Model):
    class Meta():
        db_table = "Alumni"
        verbose_name_plural = 'Alumnies'

    def __str__(self):
        return str(self.last_name) + str(' ') + str(self.first_name)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    time_in_society = models.CharField(max_length=20)
    courses = models.CharField(max_length=200)
    current_occupation = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='images', blank=True)
