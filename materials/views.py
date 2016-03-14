from django.shortcuts import render_to_response

from materials.models import Material,Event


def materials(request):
    args = {}
    return render_to_response('materials.html', args)


def material(request, id):
    args = {'material': Material.objects.get(id=id)}
    return render_to_response('material.html', args)


def events(request):
    from django.utils.datetime_safe import date
    from django.db.models import Min,Max
    today = date.today()
    start_day = Event.objects.all().aggregate(Min('when')).values()
    end_day = Event.objects.all().aggregate(Max('when')).values()
    args = {'previous': Event.objects.filter(when__range=[start_day[0],today]), 'upcoming': Event.objects.filter(when__range=[today,end_day[0]])}
    return render_to_response('events.html', args)


def event(request, id):
    args = {'event': Event.objects.get(id=id)}
    return render_to_response('event.html', args)
