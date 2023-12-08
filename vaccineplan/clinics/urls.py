from django.urls import path

import clinics.views

app_name = "clinics"

urlpatterns = [
    path(
        "registration/",
        clinics.views.ClinicRegistrationFormView.as_view(),
        name="registration",
    ),
]
