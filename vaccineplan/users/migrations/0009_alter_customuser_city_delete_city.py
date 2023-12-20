# Generated by Django 4.2 on 2023-12-20 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
        ("users", "0008_alter_city_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="city",
            field=models.ForeignKey(
                help_text="город проживания пользователя",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.city",
                verbose_name="город",
            ),
        ),
        migrations.DeleteModel(
            name="City",
        ),
    ]
