from django.shortcuts import render_to_response

from materials.models import Material,Event


def materials(request):
    args = {'workshops': Material.objects.filter(type='workshop'),
            'articles': Material.objects.filter(type='helpful article')}
    return render_to_response('materials.html', args)


def material(request, id):
    args = {'material': Material.objects.get(id=id)}
    return render_to_response('material.html', args)


def events(request):
    args = {'previous': Event.objects.filter(), 'upcoming': Event.objects.filter()}
    return render_to_response('events.html', args)


def event(request, id):
    args = {'event': Event.objects.get(id=id)}
    return render_to_response('event.html', args)
