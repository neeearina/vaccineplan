import django.db.models as models


class VaccineScheduleManager(models.Manager):
    def get_user_records(self, user):
        return self.get_queryset().filter(
            user=user,
        ).select_related(
            "clinic",
            "vaccine",
        ).only(
            "clinic__address",
            "clinic__phone_number",
            "vaccine__name",
            "timetable",
        )
