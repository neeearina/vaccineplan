import django.urls

import clinics.views

app_name = "clinics"

urlpatterns = [
    django.urls.path(
        "registration/",
        clinics.views.ClinicRegistrationFormView.as_view(),
        name="registration",
    ),
    django.urls.path(
        "<int:pk>/admin/",
        clinics.views.ClinicAdmin.as_view(),
        name="admin",
    ),
    django.urls.path(
        "<int:pk>/admin/vaccines/",
        clinics.views.clinic_vaccines,
        name="vaccines",
    ),
]
