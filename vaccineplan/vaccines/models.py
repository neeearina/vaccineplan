import django.db.models as models

import vaccines.managers


class VaccineCategories(models.Model):
    objects = vaccines.managers.VaccineCategoriesManager()

    name = models.CharField(
        max_length=100,
        help_text="название болезни",
        verbose_name="болезнь",
    )
    description = models.TextField(
        help_text="описание болезни",
        verbose_name="описание",
    )
    num_of_vaccines = models.PositiveIntegerField(
        help_text="общее количество разработанных вакцин от этой болезни",
        verbose_name="количество вакцин",
    )


class Vaccines(models.Model):
    objects = vaccines.managers.VaccinesManager()

    name = models.CharField(
        max_length=150,
        help_text="название вакцины, производство",
        verbose_name="вакцина",
    )
    category = models.ForeignKey(
        VaccineCategories,
        on_delete=models.CASCADE,
        help_text="категория вакцины - название болезни,"
        " от которой она предназначена",
        verbose_name="категория",
    )
