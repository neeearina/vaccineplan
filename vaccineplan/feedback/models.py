import django.conf
import django.db.models
import django.forms

import users.models


class Feedback(django.db.models.Model):
    class StatusChoices(django.db.models.TextChoices):
        GOT = ("GT", "получено")
        IN_POCESSING = ("PR", "в обработке")
        DONE = ("OK", "ответ дан")

    class CategoryChoices(django.db.models.TextChoices):
        QUESTION = ("QT", "вопрос")
        OFFER = ("OF", "предложение")
        OTHER = ("OR", "другое")

    name = django.db.models.CharField(
        max_length=128,
        help_text="Имя отправителя формы",
        verbose_name="имя",
        null=True,
        blank=True,
    )
    category = django.db.models.CharField(
        max_length=2,
        help_text="Категория вопроса",
        verbose_name="категория",
        choices=CategoryChoices.choices,
        default=CategoryChoices.OFFER,
    )
    text = django.db.models.TextField(
        help_text="Текст вашего сообщения",
        verbose_name="текст",
    )
    mail = django.db.models.EmailField(
        help_text="Электронный адрес, на который придёт ответ",
        verbose_name="e-mail",
    )
    status = django.db.models.CharField(
        max_length=2,
        help_text="Статус обработки формы",
        verbose_name="статус обработки",
        choices=StatusChoices.choices,
        default=StatusChoices.GOT,
    )
    created_on = django.db.models.DateTimeField(
        auto_now_add=True,
        help_text="Время создания фидбека",
        verbose_name="создано",
    )

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = "форма обратной связи"
        verbose_name_plural = "формы обратной связи"


class StatusLogFeedback(django.db.models.Model):
    user = django.db.models.ForeignKey(
        to=users.models.CustomUser,
        on_delete=django.db.models.CASCADE,
        related_name="user",
        related_query_name="user",
        help_text="пользователь, который изменил статус",
        verbose_name="пользователь",
    )
    feedback = django.db.models.ForeignKey(
        to=Feedback,
        on_delete=django.db.models.CASCADE,
        related_name="feedback",
        related_query_name="feedback",
        help_text="Фидбек",
        verbose_name="фидбек",
    )
    timestamp = django.db.models.DateTimeField(
        help_text="Время изменения статуса фидбека",
        verbose_name="время",
        auto_now_add=True,
    )
    from_status = django.db.models.CharField(
        help_text="Из какого статуса переходит фидбек",
        verbose_name="начальное состояние",
        max_length=2,
        db_column="from",
    )

    to = django.db.models.CharField(
        help_text="В какой статус переходит фидбек",
        verbose_name="новое состояние",
        max_length=2,
    )

    class Meta:
        verbose_name = "лог статусов фидбека"
        verbose_name_plural = "логи статусов фидбеков"
