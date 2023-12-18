import django.urls

import vaccines.views


app_name = "vaccines"

urlpatterns = [
    django.urls.path(
        "<int:pk>/",
        vaccines.views.VaccinesView.as_view(),
        name="vaccines",
    ),
]
