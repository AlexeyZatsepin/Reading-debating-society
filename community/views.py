from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_variables
from app.forms import SearchForm
from .models import Committee, Committee_stuff, Alumni


@cache_page(60 * 5)
def committee(request, time=''):
    years_list = sorted(list(set(Committee.objects.values_list('time', flat=True))))
    from django.utils import timezone
    today = timezone.now()
    if time == '':
        current = Committee_stuff.objects.filter(committee__time__contains=today.year)
        args = {'title': "Current committe", 'stuff': current}
    else:
        args = {'stuff': Committee_stuff.objects.filter(committee__time=time)}
        if str(today.year) in time:
            args.update({'title': "Current commitee"})
        else:
            args.update({'title': "Commitee", 'com': Committee.objects.get(time=time)})

    args.update({'years': years_list, 'search': SearchForm(), 'committee': True})
    return render_to_response('committe.html', args)


@cache_page(60 * 5)
def database(request, years='', courses='', company=''):
    years_list = sorted(list(set(Alumni.objects.values_list('time_in_society', flat=True))))
    courses_list = sorted(list(set(Alumni.objects.values_list('courses', flat=True))))
    companies_list = sorted(list(set(Alumni.objects.values_list('current_occupation', flat=True))))
    args = {'years': years_list, 'courses': courses_list, 'companies': companies_list}
    if 'thanks' in request.session:
        args.update({'thanks': request.session['thanks']})
    if years == '' and courses == '' and company == '':
        args['db'] = Alumni.objects.all()
    elif years != '':
        args['db'] = Alumni.objects.filter(time_in_society=years)
        print(years)
    elif courses != '':
        args['db'] = Alumni.objects.filter(courses=courses)
    elif company != '':
        args['db'] = Alumni.objects.filter(current_occupation=company)
    args['search'] = SearchForm()
    args['title'] = "Alumni database"
    return render_to_response('database.html', args)


@sensitive_variables('alumni')
@csrf_protect
def registration(request):
    if 'has_registrated' in request.session:
        del request.session['thanks']
        return redirect(database)
    from .forms import Registration
    from .models import Alumni
    from django.core.mail import send_mail
    form = Registration(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        alunmi = Alumni()
        alunmi.first_name = form.cleaned_data.get('first_name')
        alunmi.last_name = form.cleaned_data.get('last_name')
        alunmi.email = form.cleaned_data.get('email', None)
        alunmi.facebook = form.cleaned_data.get('facebook', None)
        alunmi.linkedin = form.cleaned_data.get('linkedin', None)
        alunmi.time_in_society = form.cleaned_data.get('time_in_society', None)
        alunmi.courses = form.cleaned_data.get('courses', None)
        alunmi.current_occupation = form.cleaned_data.get('current_occupation', None)
        #alunmi.image = request.FILES['file']
        alunmi.save()
        form.clean()
        subject = "Thanks for registration "
        message = "You are very important for our alumni community!"
        recipients = list()
        recipients.append(alunmi.email)
        recipients.append('alexzatsepin@outlook.com')
        request.session['thanks'] = subject + str(alunmi.first_name) + str(' ') + str(alunmi.last_name)
        request.session['has_registrated'] = True
        request.session.set_expiry(300)
        try:
            send_mail(subject, message, 'auto.reading.debate.society@gmail.com', recipients, fail_silently=False)
        except:
            pass
        return redirect(database)
    args = {'form': form, 'search': SearchForm(), 'title': "Register as Alumni",'regas':True}
    return render(request, 'register.html', args)
