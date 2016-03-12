from django.shortcuts import render, render_to_response
from models import Album,Photo


def gallery(request):
    args = {'albums':Album.objects.all()}
    return render_to_response('gallery.html', args)


def album(request,album_id):
    args={'photo':Photo.objects.get(album_id=album_id)}
    return render_to_response('album.html',args)
