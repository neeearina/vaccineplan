import django.conf
import django.contrib.auth.models
import django.core.validators
import django.db.models
import django.forms
import django.utils.safestring
import phonenumber_field.modelfields
import sorl.thumbnail

import core.models


class Clinics(django.db.models.Model):
    class PrivateChoices(django.db.models.TextChoices):
        PRIVATE = ("PR", "частная")
        STATE = ("ST", "государственная")

    class StatusChoices(django.db.models.TextChoices):
        GOT = ("GT", "получено")
        IN_POCESSING = ("PR", "в обработке")
        DONE = ("OK", "ответ дан")

    admin = django.db.models.ForeignKey(
        to=django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.deletion.CASCADE,
        help_text="Администратор клиники, который будет работать в профиле",
        verbose_name="администратор",
    )
    image = django.db.models.ImageField(
        upload_to="catalog/%Y/%m/%d/",
        help_text="Главное изображение поликлиники",
        verbose_name="изображение",
        null=True,
        blank=True,
    )
    name = django.db.models.CharField(
        max_length=256,
        help_text="Название клиники",
        verbose_name="клиника",
    )
    city = django.db.models.ForeignKey(
        to=core.models.City,
        help_text="город/населенный пункт, в котором находится клиника",
        verbose_name="город",
        on_delete=django.db.models.deletion.CASCADE,
    )
    address = django.db.models.CharField(
        max_length=128,
        help_text="Адрес, где находится клиника",
        verbose_name="адрес",
        validators=[
            django.core.validators.MinLengthValidator(
                15,
                message="Слишком короткий текст.",
            ),
        ],
    )
    lisense = django.db.models.CharField(
        max_length=256,
        help_text="Лицензия на медицинскую деятельность",
        verbose_name="лицензия",
        validators=[
            django.core.validators.MinLengthValidator(
                10,
                message="Слишком короткий текст.",
            ),
        ],
    )
    phone_number = phonenumber_field.modelfields.PhoneNumberField(
        region="RU",
        help_text="Номер телефона для связи с администратором клиники",
        verbose_name="номер телефона",
        error_messages={
            "invalid": "Пожалуйста, введите корректный номер телефона.",
        },
    )
    status = django.db.models.CharField(
        max_length=2,
        help_text="Статус обработки формы",
        verbose_name="статус обработки",
        choices=StatusChoices.choices,
        default=StatusChoices.GOT,
    )
    approved = django.db.models.BooleanField(
        default=False,
        help_text="Одобрена поликлиника для работы на сайте или нет",
        verbose_name="одобрено",
    )
    clinic_mail = django.db.models.EmailField(
        help_text="Электронная почта клиники",
        verbose_name="почта",
    )
    private = django.db.models.CharField(
        max_length=2,
        help_text="Частная или приватная клиника",
        verbose_name="частная или приватная",
        choices=PrivateChoices.choices,
        default=PrivateChoices.STATE,
    )

    class Meta:
        verbose_name = "клиника"
        verbose_name_plural = "клиники"

    def __str__(self):
        return self.name

    def get_image_x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def get_image_x50(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "50x50",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_image_x300().url}">',
            )
        return "изображения нет"


class StatusLog(django.db.models.Model):
    user = django.db.models.ForeignKey(
        to=django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        related_name="user",
        related_query_name="user",
        help_text="пользователь, который изменил статус",
        verbose_name="пользователь",
    )

    clinic = django.db.models.ForeignKey(
        to=Clinics,
        on_delete=django.db.models.CASCADE,
        help_text="заявка, в которой поменялся статус",
        verbose_name="заявка",
    )

    timestamp = django.db.models.DateTimeField(
        auto_now_add=True,
        help_text="когда был создан лог",
        verbose_name="лог",
    )

    from_status = django.db.models.CharField(
        max_length=2,
        db_column="from",
        help_text="из какого статуса перешла заявка",
        verbose_name="начальное состояние",
    )

    to = django.db.models.CharField(
        max_length=2,
        help_text="в какой статус перешла заявка",
        verbose_name="новое состояние",
    )

    class Meta:
        verbose_name = "лог статусов"
        verbose_name_plural = "логи статусов"

    def __str__(self):
        return f"лог #{self.id}"
