import django.db.models


class VaccineCategoriesManager(django.db.models.Manager):
    pass


class VaccinesManager(django.db.models.Manager):
    pass


class AvaliabilityManager(django.db.models.Manager):
    def get_by_illness(self, illness):
        return self.get_queryset().filter(vaccines__category=illness)
