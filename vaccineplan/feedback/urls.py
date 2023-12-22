import django.urls

import feedback.views

app_name = "feedback"

urlpatterns = [
    django.urls.path(
        "",
        feedback.views.FeedbackFormView.as_view(),
        name="feedback",
    ),
]
