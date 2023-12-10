import django.shortcuts
import django.views.generic

import vaccine_calendar.models


class VaccineCalendarView(django.views.generic.ListView):
    model = vaccine_calendar.models.Schedule
    template_name = "vaccine_calendar/list.html"
