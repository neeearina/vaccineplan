import django.core.validators
import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control my-1"
            field.field.widget.attrs["placeholder"] = field.field.label
        self.fields["name"].required = False
        self.fields["category"].required = False
        self.fields["name"].widget = django.forms.Textarea()
        self.fields["text"].widget = django.forms.Textarea()
        self.fields["mail"].widget = django.forms.EmailInput()

    mail = django.forms.EmailField(
        label="E-mail",
        help_text="Электронный адрес, на который придёт ответ",
        validators=[
            django.core.validators.EmailValidator(
                message="Некорректный e-mail адрес",
            ),
        ],
    )

    class Meta:
        model = feedback.models.Feedback
        exclude = [
            feedback.models.Feedback.status.field.name,
            feedback.models.Feedback.created_on.field.name,
            feedback.models.Feedback.mail.field.name,
        ]
