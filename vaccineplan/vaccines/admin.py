import django.contrib

import vaccines.models


django.contrib.admin.site.register(vaccines.models.VaccineCategories)
django.contrib.admin.site.register(vaccines.models.Vaccines)
django.contrib.admin.site.register(vaccines.models.Availability)
