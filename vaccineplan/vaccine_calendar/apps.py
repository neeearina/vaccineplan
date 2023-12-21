import django.apps
import scheduler


class VaccineCalendarConfig(django.apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "vaccine_calendar"

    def ready(self):
        scheduler.start()
