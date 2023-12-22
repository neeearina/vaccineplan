import django.db.models


class AvaliabilityManager(django.db.models.Manager):
    def get_by_illness(self, illness):
        return (
            self.get_queryset()
            .filter(
                vaccines__category=illness,
            )
            .filter(
                clinic__approved=True,
            )
        )

    def get_already_checked(self, clinic):
        return (
            self.get_queryset()
            .filter(
                clinic=clinic,
            )
            .select_related("vaccines")
            .only("vaccines__id")
        )
