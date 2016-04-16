from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.core.urlresolvers import reverse

from gallery.models import Album

info_dict = {
    'queryset': Album.objects.all(),
    'date_field': 'year',
}


class MainSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ['welcome', 'debating']

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['search','sponsors','contact','materials','events','workshops','database','registr','committee','gallery']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'main': MainSitemap,
    'static': StaticViewSitemap,
    'albums': GenericSitemap(info_dict, priority=0.5)
}