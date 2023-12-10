import django.db.models

import users.models
import vaccine_calendar.managers
import vaccines.models


class Schedule(django.db.models.Model):
    objects = vaccine_calendar.managers.VaccineCategoriesManager()

    vaccine = django.db.models.ForeignKey(
        vaccines.models.Vaccines,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="вакцина",
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        null=True,
        verbose_name="пользователь",
    )
    timetable = django.db.models.DateTimeField(
        verbose_name="расписание",
    )
