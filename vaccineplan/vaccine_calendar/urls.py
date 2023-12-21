import django.urls

import vaccine_calendar.views


app_name = "vaccine_calendar"

urlpatterns = [
    django.urls.path(
        "",
        vaccine_calendar.views.VaccineCalendarView.as_view(),
        name="calendar",
    ),
    django.urls.path(
        "record/<int:pk>",
        vaccine_calendar.views.RecordView.as_view(),
        name="record",
    ),
    django.urls.path(
        "record/<int:pk>/delete",
        vaccine_calendar.views.RecordDeleteView.as_view(),
        name="record_delete",
    ),
]
