import django.db.models

import clinics.models


class VaccineCategories(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=100,
        help_text="название болезни",
        verbose_name="болезнь",
    )
    description = django.db.models.TextField(
        blank=True,
        help_text="описание болезни",
        verbose_name="описание",
    )
    num_of_vaccines = django.db.models.PositiveIntegerField(
        default=0,
        blank=True,
        help_text="общее количество разработанных вакцин от этой болезни",
        verbose_name="количество вакцин",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return f"Категория вакцины {self.name}"


class Vaccines(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=150,
        help_text="название вакцины, производство",
        verbose_name="вакцина",
    )
    category = django.db.models.ForeignKey(
        VaccineCategories,
        on_delete=django.db.models.CASCADE,
        help_text="категория вакцины - название болезни,"
        " от которой она предназначена",
        verbose_name="категория",
    )

    class Meta:
        verbose_name = "вакцина"
        verbose_name_plural = "вакцины"

    def __str__(self):
        return f"Вакцина {self.name}"


class Availability(django.db.models.Model):
    vaccines = django.db.models.ForeignKey(
        Vaccines,
        help_text="название имеющейся вакцины в поликлинике",
        verbose_name="вакцина",
        on_delete=django.db.models.CASCADE,
    )

    clinic = django.db.models.ForeignKey(
        clinics.models.Clinics,
        help_text="поликлинка, в которой находится вакцина",
        verbose_name="вакцина",
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        verbose_name = "Наличие"
        verbose_name_plural = "Наличия"
