from django.shortcuts import render_to_response, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .forms import *
from .models import *
from staticArticles.models import Flatblock
from materials.models import Material, Event
from gallery.models import Album


def search_form(func):
    def wrapped(**kwargs):
        form = SearchForm()
        kwargs = {'search': form}
        return func(**kwargs)

    return wrapped


def counter():
    visit = Visits()
    visit.save()


# @counter
# @search_form


@cache_page(60 * 10)
def index(request):
    counter()
    args = {'slider': Slider.objects.all(), 'flatblock': Flatblock.objects.get(title='welcome'),
            'search': SearchForm(), 'title': "Reading Debating Society"}
    return render_to_response('welcome.html', args)


@cache_page(60 * 10)
def debating(request):
    args = {'flatblock': Flatblock.objects.get(title='debating'), 'search': SearchForm(), 'title': "Debating",
            'debating': True}
    return render_to_response('debating.html', args)


@cache_page(60 * 5)
def sponsors(request):
    args = {'sponsors': Sponsor.objects.all(), 'search': SearchForm(), 'title': "Our sponsors", 'sponsors_page': True}
    return render_to_response('sponsors.html', args)


@csrf_protect
def contact(request):
    from django.core.mail import send_mail
    # args.update(csrf(request))
    form = ContactForm(request.POST or None)
    args = {'form': form, 'search': SearchForm(), 'title': "Contact us", 'contact': True}
    if form.is_valid() and request.method == 'POST':
        subject = form.cleaned_data['subject']
        sender = form.cleaned_data['sender']
        message = form.cleaned_data['message']
        recipients = ['alexzatsepin@outlook.com']
        try:
            send_mail(subject, message, 'alexzatsepin7@gmail.com', recipients, fail_silently=False)
            thanks = "Thank you %s! Your message was successfully sent." % sender
            args.update({'thanks': thanks})
        except:
            args['thanks'] = 'Try again, server overload'
    return render(request, 'contact.html', args)


@csrf_protect
def search(request):
    from django.db.models import Q
    title = "Search of %s" % request.GET['field']
    materials_result = Material.objects.filter(Q(title__contains=request.GET['field']))
    events_result = Event.objects.filter(
        Q(title__contains=request.GET['field']) | Q(when__contains=request.GET['field']) |
        Q(short_discription__contains=request.GET['field']))
    gallery_result = Album.objects.filter(
        Q(title__contains=request.GET['field']) | Q(year__contains=request.GET['field']))
    args = {'materials': materials_result, 'events': events_result, 'albums': gallery_result, 'search': SearchForm(),
            'title': title}
    return render_to_response('search.html', args)


'''
def info(request):
    from qsstats import QuerySetStats
    from django.db.models import Count,Min
    from django.utils import timezone
    args={}
    today=timezone.now()
    start_day = Visits.objects.all().aggregate(Min('datetime')).values()
    qsstats = QuerySetStats(Visits.objects.all(), date_field='datetime', aggregate=Count('id'))
    values = qsstats.time_series(start_day[0], today, interval='days')
    args['values']=values
    return render_to_response('info.html',args)
'''
