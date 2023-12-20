import django.shortcuts
import django.views.generic

import vaccines.models


class HomepageView(django.views.generic.ListView):
    # model = vaccines.models.VaccineCategories
    context_object_name = "illnesses"
    template_name = "homepage/homepage.html"
    queryset = vaccines.models.VaccineCategories.objects.all()
