import django.urls

import vaccine_calendar.views


app_name = "vaccine_calendar"

urlpatterns = [
    django.urls.path(
        "",
        vaccine_calendar.views.VaccineCalendarView.as_view(),
        name="list",
    ),
    django.urls.path(
        "record/<int:pk>",
        vaccine_calendar.views.RecordView.as_view(),
        name="record",
    ),
]
