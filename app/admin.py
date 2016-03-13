from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.contrib.auth.models import Group
from django.views.decorators.cache import never_cache

from .models import  Sponsor, Slider, Visits


class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image',)
    view_on_site = False


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name')
    search_fields = ['name']


from django.contrib.admin import AdminSite


class VisitManager(admin.ModelAdmin):
    @csrf_protect_m
    def changelist_view(self, request, **kwargs):
        from qsstats import QuerySetStats
        from django.db.models import Count, Min
        from django.utils import timezone
        today = timezone.now()
        start_day = Visits.objects.all().aggregate(Min('datetime')).values()
        print(start_day[0])
        print(today)
        qsstats = QuerySetStats(Visits.objects.all(), date_field='datetime', aggregate=Count('id'))
        values = qsstats.time_series(start_day[0], today, interval='days')
        args = {'values': values,'opts': Visits._meta, 'app_label': Visits._meta.app_label, 'site_header': 'Welcome page visits statistic', 'site_title': "Statistic"}
        from django.shortcuts import render_to_response
        from django.template import RequestContext
        return render_to_response('admin/app/visits/change_list.html', args, context_instance=RequestContext(request))


admin.site.index_title = 'Administrating'
admin.site.site_title = "Reading Debate Society Admin page"
admin.site.site_header = "Reading Debate Society Admin page"
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.unregister(Group)
admin.site.register(Visits, VisitManager)
