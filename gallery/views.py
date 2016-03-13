from django.shortcuts import render_to_response
from models import Album,Photo


def gallery(request, year=''):
    years_list = sorted(list(set(Album.objects.values_list('year',flat=True))))
    if year == '':
        args = {'albums': Album.objects.all()}
    else:
        args = {'albums': Album.objects.filter(year=year)}
    args.update({'years': years_list})
    return render_to_response('gallery.html', args)


def album(request, id):
    args={'photos':Photo.objects.filter(album_id=id)}
    return render_to_response('album.html',args)
