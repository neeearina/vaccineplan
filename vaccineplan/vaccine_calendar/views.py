import datetime

from typing import Any
from django.db.models.query import QuerySet
import django.shortcuts
import django.utils
import django.views.generic

import vaccine_calendar.models


class VaccineCalendarView(django.views.generic.ListView):
    model = vaccine_calendar.models.Schedule
    template_name = "vaccine_calendar/list.html"

    ordering = ["-timetable"]

    def get_queryset(self) -> QuerySet[Any]:
        return (
            super()
            .get_queryset()
            .filter(user=self.request.user.id)
            # Добавить поддержку часовых поясов
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = django.utils.timezone.now()
        return context
