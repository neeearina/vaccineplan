import django.conf
import django.contrib.auth.models
import django.core.validators
import django.db.models
import django.utils.safestring
import phonenumber_field.modelfields
import sorl.thumbnail


class Clinics(django.db.models.Model):
    class StatusChoices(django.db.models.TextChoices):
        GOT = ("GT", "получено")
        IN_POCESSING = ("PR", "в обработке")
        DONE = ("OK", "ответ дан")

    admin = django.db.models.ForeignKey(
        django.contrib.auth.models.User,
        on_delete=django.db.models.deletion.CASCADE,
        help_text="Администратор клиники, который будет работать в профиле",
        verbose_name="администратор",
    )
    name = django.db.models.CharField(
        max_length=256,
        help_text="Название клиники",
        verbose_name="клиника",
    )
    city = django.db.models.CharField(
        max_length=128,
        help_text="Город/населенный пункт, в котором находится клиника",
        verbose_name="место",
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
        "статус обработки",
        max_length=2,
        help_text="статус обработки формы",
        choices=StatusChoices.choices,
        default=StatusChoices.GOT,
    )
    approved = django.db.models.BooleanField(
        default=False,
        help_text="одобрена поликлиника для работы на сайте или нет",
        verbose_name="одобрено",
    )
    clinic_mail = django.db.models.EmailField(
        help_text="Электронная почта клиники",
        verbose_name="почта",
    )

    class Meta:
        verbose_name = "клиника"
        verbose_name_plural = "клиники"

    def __str__(self):
        return f"Заявка {self.id}"

    def get_image_x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.main_image.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def get_image_x50(self):
        return sorl.thumbnail.get_thumbnail(
            self.main_image.image,
            "50x50",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.main_image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_image_x300().url}">',
            )
        return "изображения нет"


class MainImage(django.db.models.Model):
    image = django.db.models.ImageField(
        upload_to="catalog/%Y/%m/%d/",
        help_text="главное изображение поликлиники",
        verbose_name="изображение",
    )
    clinic = django.db.models.OneToOneField(
        Clinics,
        on_delete=django.db.models.deletion.CASCADE,
        related_name="main_image",
        help_text="к какой клинике прикреплено фото",
        verbose_name="клиника",
        null=True,
    )

    class Meta:
        verbose_name = "главное изображение"
        verbose_name_plural = "главные изображения"


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
        return f"лог {self.id}"
