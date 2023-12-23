import django.db.models

import clinics.models
import vaccines.managers


class VaccineCategories(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=100,
        help_text="название болезни",
        verbose_name="болезнь",
        unique=True,
    )
    description = django.db.models.TextField(
        blank=True,
        help_text="описание болезни",
        verbose_name="описание",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return f"Категория вакцины: {self.name}"


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
    objects = vaccines.managers.AvaliabilityManager()

    vaccines = django.db.models.ForeignKey(
        Vaccines,
        help_text="название имеющейся вакцины в поликлинике",
        verbose_name="вакцина",
        on_delete=django.db.models.CASCADE,
    )

    clinic = django.db.models.ForeignKey(
        clinics.models.Clinics,
        help_text="поликлинка, в которой находится вакцина",
        verbose_name="клиника",
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        verbose_name = "наличие"
        verbose_name_plural = "наличия"
