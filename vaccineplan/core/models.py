import django.db.models


class City(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название города",
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"
