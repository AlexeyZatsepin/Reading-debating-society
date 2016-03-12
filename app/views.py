from django.shortcuts import render_to_response, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .forms import *
from .models import *
from staticArticles.models import Flatblock


def counter():
    visit = Visits()
    visit.save()
    return True


@cache_page(60 * 3)
def index(request):
    counter()
    args = {'slider': Slider.objects.all(), 'flatblock': Flatblock.objects.get(title='welcome')}
    return render_to_response('welcome.html', args)


def debating(request):
    args = {'flatblock': Flatblock.objects.get(title='debating')}
    return render_to_response('debating.html', args)


def sponsors(request):
    args = {'sponsors': Sponsor.objects.all()}
    return render_to_response('sponsors.html', args)


@csrf_protect
def contact(request):
    from django.core.mail import send_mail
    # args.update(csrf(request))
    form = ContactForm(request.POST or None)
    args = {'form': form}
    if form.is_valid() and request.method == 'POST':
        subject = form.cleaned_data['subject']
        sender = form.cleaned_data['sender']
        message = form.cleaned_data['message']
        recipients = ['alexzatsepin@outlook.com']
        thanks = "Thank you %s" % sender
        args = {'thanks': thanks}
        try:
            send_mail(subject, message, 'alexzatsepin7@gmail.com', recipients, fail_silently=False)
        except:
            args['thanks'] = 'Try again, server overload'
            return render(request, 'contact.html', args)
    return render(request, 'contact.html', args)


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
