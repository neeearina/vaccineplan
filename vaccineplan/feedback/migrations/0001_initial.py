# Generated by Django 4.2 on 2023-12-22 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Имя отправителя формы",
                        max_length=128,
                        null=True,
                        verbose_name="имя",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("QT", "вопрос"),
                            ("OF", "предложение"),
                            ("OR", "другое"),
                        ],
                        default="OF",
                        help_text="Категория вопроса",
                        max_length=2,
                        verbose_name="категория",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Текст вашего сообщения",
                        verbose_name="текст",
                    ),
                ),
                (
                    "mail",
                    models.EmailField(
                        help_text="Электронный адрес, на который придёт ответ",
                        max_length=254,
                        verbose_name="e-mail",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("GT", "получено"),
                            ("PR", "в обработке"),
                            ("OK", "ответ дан"),
                        ],
                        default="GT",
                        help_text="Статус обработки формы",
                        max_length=2,
                        verbose_name="статус обработки",
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Время создания фидбека",
                        verbose_name="создано",
                    ),
                ),
            ],
            options={
                "verbose_name": "форма обратной связи",
                "verbose_name_plural": "формы обратной связи",
            },
        ),
        migrations.CreateModel(
            name="StatusLogFeedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Время изменения статуса фидбека",
                        verbose_name="время",
                    ),
                ),
                (
                    "from_status",
                    models.CharField(
                        db_column="from",
                        help_text="Из какого статуса переходит фидбек",
                        max_length=2,
                        verbose_name="начальное состояние",
                    ),
                ),
                (
                    "to",
                    models.CharField(
                        help_text="В какой статус переходит фидбек",
                        max_length=2,
                        verbose_name="новое состояние",
                    ),
                ),
                (
                    "feedback",
                    models.ForeignKey(
                        help_text="Фидбек",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback",
                        related_query_name="feedback",
                        to="feedback.feedback",
                        verbose_name="фидбек",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="пользователь, который изменил статус",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        related_query_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "лог статусов фидбека",
                "verbose_name_plural": "логи статусов фидбеков",
            },
        ),
    ]