import django.db.models


class AvaliabilityManager(django.db.models.Manager):
    def get_by_illness(self, illness):
        return self.get_queryset().filter(vaccines__category=illness)
