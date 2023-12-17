import django.urls

import vaccines.views


app_name = "vaccines"

urlpatterns = [
    django.urls.path(
        "<int:pk>/",
        vaccines.views.HomepageView.as_view(),
        name="vaccines",
    ),
]
