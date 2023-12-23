import django.contrib.auth.mixins
import django.db.models.query
import django.http
import django.shortcuts
import django.urls
import django.utils
import django.views.generic

import vaccine_calendar.forms
import vaccine_calendar.models
import vaccines.models


class VaccineCalendarView(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.ListView,
):
    model = vaccine_calendar.models.Schedule
    template_name = "vaccine_calendar/list.html"

    ordering = ["timetable"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = django.utils.timezone.now()
        return context


class RecordView(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.edit.FormView,
    django.views.generic.DetailView,
):
    model = vaccines.models.Availability
    form_class = vaccine_calendar.forms.CalendarDateTimeForm
    template_name = "vaccine_calendar/availability.html"
    success_url = django.urls.reverse_lazy("vaccine_calendar:calendar")

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return django.http.HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        vaccine_calendar.models.Schedule.objects.create(
            vaccine=self.object.vaccines,
            clinic=self.object.clinic,
            user=self.request.user,
            timetable=form.cleaned_data["date"],
        )
        return super().form_valid(form)


class RecordDeleteView(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.edit.DeleteView,
):
    model = vaccine_calendar.models.Schedule
    success_url = django.urls.reverse_lazy("vaccine_calendar:calendar")
    template_name = "vaccine_calendar/record_delete.html"
