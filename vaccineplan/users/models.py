import pathlib

import django.contrib.auth.models
import django.core.validators
import django.db.models
import sorl

import clinics.models


class CustomUser(django.contrib.auth.models.AbstractUser):
    def get_avatar_path(self, filename):
        return (
            pathlib.Path("users")
            / f"avatar_user_{str(self.user.id)}.{filename.split('.')[-1]}"
        )

    class GenderChoices(django.db.models.TextChoices):
        MALE = ("M", "мужской")
        FEMALE = ("F", "женский")

    gender = django.db.models.CharField(
        "пол",
        max_length=1,
        choices=GenderChoices.choices,
    )

    birthday = django.db.models.DateField(
        "дата рождения",
        blank=True,
        null=True,
    )

    image = django.db.models.ImageField(
        "аватарка",
        blank=True,
        null=True,
        upload_to=get_avatar_path,
    )

    middle_name = django.db.models.CharField(
        "отчество",
        blank=True,
        null=True,
        max_length=128,
    )

    clinic = django.db.models.ForeignKey(
        to=clinics.models.Clinics,
        verbose_name="клиника",
        help_text="клиника, к которой прикреплен пользователь",
        blank=True,
        null=True,
        on_delete=django.db.models.deletion.CASCADE,
    )

    def get_image_x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_image_x300().url}">',
            )
        return "изображения нет"

    image_tmb.short_description = "превью (300x300)"
    image_tmb.allow_tags = True
