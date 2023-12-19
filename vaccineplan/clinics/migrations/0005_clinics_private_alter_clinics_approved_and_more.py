# Generated by Django 4.2 on 2023-12-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinics", "0004_clinics_approved_clinics_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="clinics",
            name="private",
            field=models.BooleanField(
                default=False,
                help_text="Галочка, если клиника частная",
                verbose_name="частная клиника",
            ),
        ),
        migrations.AlterField(
            model_name="clinics",
            name="approved",
            field=models.BooleanField(
                default=False,
                help_text="Одобрена поликлиника для работы на сайте или нет",
                verbose_name="одобрено",
            ),
        ),
        migrations.AlterField(
            model_name="clinics",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Главное изображение поликлиники",
                null=True,
                upload_to="catalog/%Y/%m/%d/",
                verbose_name="изображение",
            ),
        ),
        migrations.AlterField(
            model_name="clinics",
            name="status",
            field=models.CharField(
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
    ]