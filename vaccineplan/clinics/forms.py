import django.core.validators
import django.forms

import clinics.models


class ClinicsForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control my-1"
            field.field.widget.attrs["placeholder"] = field.field.label

    name = django.forms.CharField(
        label="название клиники",
        help_text="название клиники, на которую подается заявка",
    )
    city = django.forms.CharField(
        label="город",
        help_text="город/населенный пункт, в котором находится клиника",
    )
    address = django.forms.CharField(
        label="адрес клиники",
        help_text="адрес, где находится клиника",
    )
    lisense = django.forms.CharField(
        label="лицензия",
        help_text="лицензия на медицинскую деятельность",
    )
    phone_number = django.forms.CharField(
        label="номер телефона",
        help_text="номер телефона клиники для связи с администратором",
    )
    clinic_mail = django.forms.EmailField(
        label="электронная почта",
        help_text="электронная почта клиники",
        validators=[
            django.core.validators.EmailValidator(
                message="некорректный адрес электронной почты",
            ),
        ],
    )

    class Meta:
        model = clinics.models.Clinics
        exclude = [
            clinics.models.Clinics.admin.field.name,
            clinics.models.Clinics.status.field.name,
        ]
