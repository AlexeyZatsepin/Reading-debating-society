from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.cache import cache_page

from app.forms import SearchForm, SearchFormMobile
from .models import Album, Photo


@cache_page(60 * 10)
def gallery(request, year=''):
    years_list = sorted(list(set(Album.objects.values_list('year', flat=True))))
    if year == '':
        args = {'albums': Album.objects.all()}
    else:
        args = {'albums': Album.objects.filter(year=year)}
    args.update({'years': years_list, 'search': SearchForm(), 'searchMobile': SearchFormMobile(),'gallery': True, 'title': "Photo gallery"})
    return render_to_response('gallery.html', args)


@cache_page(60 * 10)
def album(request, id):
    title = "Album %s" % Album.objects.get(id=id).title
    args = {'photos': get_list_or_404(Photo, album_id=id, ), 'gallery': True, 'title': title, 'search': SearchForm(), 'searchMobile':SearchFormMobile(),
            'preload': True}
    return render_to_response('album.html', args)
