import django.shortcuts
import django.views.generic

import vaccines.models


class VaccinesView(django.views.generic.ListView):
    template_name = "vaccines/vaccines_list.html"
    context_object_name = "free_vaccines"

    def get_queryset(self):
        return vaccines.models.Availability.objects.get_by_illness(
            self.kwargs["pk"],
        ).filter(
            is_free=True,
            clinic=self.request.user.clinic,
        )

    def get_context_data(self, *args, **kwargs):
        context = super(VaccinesView, self).get_context_data(*args, **kwargs)
        context["illness"] = vaccines.models.VaccineCategories.objects.get(
            id=self.kwargs["pk"],
        )
        context[
            "paid_vaccines"
        ] = vaccines.models.Availability.objects.get_by_illness(
            self.kwargs["pk"],
        ).filter(
            is_free=False,
        )
        return context
