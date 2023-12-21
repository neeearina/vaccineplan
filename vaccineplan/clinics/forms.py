import django.forms

import clinics.models


class ClinicsForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control my-1"
            field.field.widget.attrs["placeholder"] = field.field.label
            field.field.required = True
        self.fields["image"].required = False
        self.fields["private"].required = False

    class Meta:
        model = clinics.models.Clinics
        fields = "__all__"
        exclude = [
            clinics.models.Clinics.admin.field.name,
            clinics.models.Clinics.approved.field.name,
            clinics.models.Clinics.status.field.name,
        ]


class ClinicEditForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control my-1"
        self.fields[
            clinics.models.Clinics.image.field.name
        ].widget = django.forms.FileInput()

    class Meta:
        model = clinics.models.Clinics
        fields = "__all__"
        exclude = [
            clinics.models.Clinics.admin.field.name,
            clinics.models.Clinics.approved.field.name,
            clinics.models.Clinics.status.field.name,
            clinics.models.Clinics.lisense.field.name,
        ]
