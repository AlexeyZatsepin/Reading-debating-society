from django.shortcuts import render_to_response
import os
from django.views.decorators.cache import cache_page

from app.forms import SearchForm, SearchFormMobile
from config import settings
from materials.models import Material, Event


@cache_page(60 * 3)
def materials(request):
    args = {'materials': Material.objects.all(), 'search': SearchForm(), 'searchMobile': SearchFormMobile(), 'title': "Helpful articles",'lm':True}
    return render_to_response('materials.html', args)


@cache_page(60 * 10)
def events(request):
    from django.utils.datetime_safe import date
    from django.db.models import Min, Max
    today = date.today()
    start_day = Event.objects.all().aggregate(Min('when')).values()
    end_day = Event.objects.all().aggregate(Max('when')).values()
    args = {'previous': Event.objects.filter(when__range=[start_day[0], today]),
            'upcoming': Event.objects.filter(when__range=[today, end_day[0]]),
            'search': SearchForm(), 'searchMobile': SearchFormMobile(), 'title':"Events",'e': True}
    return render_to_response('events.html', args)


def event(request, id):
    args = {'event': Event.objects.get(id=id), 'search': SearchForm(), 'searchMobile': SearchFormMobile()}
    return render_to_response('event.html', args)


def download(request, file_name):
    file_path = settings.MEDIA_ROOT + '/' + file_name
    from wsgiref.util import FileWrapper
    import mimetypes
    from django.http import HttpResponse
    file_wrapper = FileWrapper(file(file_path, 'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    from django.utils.encoding import smart_str
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    return response
