import django.db.models

import clinics.models
import users.models
import vaccine_calendar.managers
import vaccines.models


class Schedule(django.db.models.Model):
    objects = vaccine_calendar.managers.VaccineScheduleManager()

    vaccine = django.db.models.ForeignKey(
        vaccines.models.Vaccines,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="вакцина",
    )
    clinic = django.db.models.ForeignKey(
        clinics.models.Clinics,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="клиника",
    )
    user = django.db.models.ForeignKey(
        users.models.CustomUser,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="пользователь",
    )
    timetable = django.db.models.DateTimeField(
        verbose_name="расписание",
    )
