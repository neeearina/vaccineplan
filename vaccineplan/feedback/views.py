import django.conf
import django.contrib.messages
import django.core.mail
import django.shortcuts
import django.urls
import django.views.generic

import feedback.forms
import feedback.models


class FeedbackFormView(django.views.generic.FormView):
    template_name = "feedback/feedback.html"
    form_class = feedback.forms.FeedbackForm
    success_url = django.urls.reverse_lazy("feedback:feedback")

    def form_valid(self, form):
        new_feedback = feedback.models.Feedback(**form.cleaned_data)
        new_feedback.save()

        django.core.mail.send_mail(
            "FROM: {}".format(new_feedback.mail),
            new_feedback.text,
            django.conf.settings.EMAIL_ADDRESS,
            [new_feedback.mail],
            fail_silently=False,
        )

        django.contrib.messages.success(
            request=self.request,
            message="Форма успешно отправлена! Спасибо за Ваш отзыв!",
        )

        return super().form_valid(form)
