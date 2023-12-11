import django.apps


class ClinicsConfig(django.apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "clinics"
    verbose_name = "клиника"
    verbose_name_plural = "клиники"
