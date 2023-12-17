import django.shortcuts
import django.views.generic

import vaccines.models


class VaccinesView(django.views.generic.ListView):
    context_object_name = "illnesses"
    template_name = "homepage/homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = {}
        context["free_vaccines"] = vaccines.models.Availiability.objects
        .filter(clinic=user.clinic)
        context['alphabetical_poll_list'] = vaccines.models.VaccineCategories.objects.filter
        return context 
