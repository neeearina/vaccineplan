from django.contrib import admin

import clinics.models


@admin.register(clinics.models.Clinics)
class ClinicsAdmin(admin.ModelAdmin):
    list_display = (
        clinics.models.Clinics.name.field.name,
        clinics.models.Clinics.city.field.name,
        clinics.models.Clinics.status.field.name,
    )
    readonly_fields = (
        clinics.models.Clinics.name.field.name,
        clinics.models.Clinics.admin.field.name,
        clinics.models.Clinics.city.field.name,
        clinics.models.Clinics.address.field.name,
        clinics.models.Clinics.lisense.field.name,
        clinics.models.Clinics.phone_number.field.name,
        clinics.models.Clinics.clinic_mail.field.name,
    )

    def save_model(self, request, obj, form, change):
        if change and form.cleaned_data["status"] != form.initial.get(
            "status",
        ):
            clinics.models.StatusLog.objects.create(
                user=request.user,
                from_status=form.initial.get("status"),
                to=form.cleaned_data.get("status"),
                clinic=obj,
            )

        super().save_model(request, obj, form, change)


@admin.register(clinics.models.StatusLog)
class StatusLogAdmin(admin.ModelAdmin):
    list_display = (
        clinics.models.StatusLog.user.field.name,
        clinics.models.StatusLog.from_status.field.name,
        clinics.models.StatusLog.to.field.name,
    )

    readonly_fields = (
        clinics.models.StatusLog.clinic.field.name,
        clinics.models.StatusLog.user.field.name,
        clinics.models.StatusLog.timestamp.field.name,
        clinics.models.StatusLog.from_status.field.name,
        clinics.models.StatusLog.to.field.name,
    )
