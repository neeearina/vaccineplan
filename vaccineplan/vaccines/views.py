import django.shortcuts
import django.views.generic

import vaccines.models


class VaccinesView(django.views.generic.ListView):
    template_name = "vaccines/vaccines_list.html"
    context_object_name = "free_vaccines"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.clinic:
                return vaccines.models.Availability.objects.get_by_illness(
                    self.kwargs["pk"],
                ).filter(
                    clinic=self.request.user__clinic,
                )
        return []

    def get_context_data(self, *args, **kwargs):
        context = super(VaccinesView, self).get_context_data(*args, **kwargs)
        context["illness"] = vaccines.models.VaccineCategories.objects.get(
            id=self.kwargs["pk"],
        )
        paid_vaccines = vaccines.models.Availability.objects.get_by_illness(
            self.kwargs["pk"],
        )
        # if self.request.user.id:
        #     paid_vaccines = paid_vaccines.filter(
        #         clinic__city=self.request.user__city,
        #     )
        context["paid_vaccines"] = paid_vaccines.order_by("clinic__id")
        return context
