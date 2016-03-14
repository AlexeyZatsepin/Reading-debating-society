from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, BadHeaderError
from django.views.decorators.debug import sensitive_variables

from .models import Committee, Committee_stuff, Alumni


def committee(request, time=''):
    years_list = sorted(list(set(Committee.objects.values_list('time', flat=True))))
    if time == '':
        args = {'stuff': Committee_stuff.objects.all()}
    else:
        args = {'stuff': Committee_stuff.objects.filter(committee__time=time)}
    args.update({'years': years_list})
    return render_to_response('committe.html', args)


def database(request, ):
    thanks = request.session['thanks']
    args = {'thanks': thanks if thanks else None, 'db': Alumni.objects.all()}
    return render_to_response('database.html', args)


@sensitive_variables('alumni')
@csrf_protect
def registration(request):
    from .forms import Registration
    from .models import Alumni
    from django.core.mail import send_mail
    form = Registration(request.POST or None)
    args = {'form': form}
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
        alunmi.save()
        subject = "Thanks for registration "
        message = "You are very important for our alumni community!"
        recipients = list()
        recipients.append(alunmi.email)
        try:
            send_mail(subject, message, 'alexzatsepin7@gmail.com', recipients, fail_silently=False)
        except BadHeaderError:
            args['thanks'] = 'Try again, server overload'
            return render(request, 'register.html', args)
        request.session['thanks'] = subject + str(alunmi.first_name) + str(' ') + str(alunmi.last_name)
        return redirect(database)
    return render(request, 'register.html', args)
