import django.conf
import django.contrib.messages
import django.core.mail
import django.shortcuts
import django.urls
import django.views.generic

import clinics.forms
import clinics.models

__all__ = []


class ClinicRegistrationFormView(django.views.generic.FormView):
    template_name = "clinics/registration.html"
    form_class = clinics.forms.ClinicsForm
    success_url = django.urls.reverse_lazy("clinics:registration")

    def form_valid(self, form):
        new_clinic = clinics.models.Clinics(**form.cleaned_data)
        new_clinic.admin = self.request.user
        new_clinic.save()
        django.contrib.messages.success(
            request=self.request,
            message="Форма успешно отправлена!"
            "Вы получите письмо на почту, когда заявку одобрят.",
        )
        return super().form_valid(form)
