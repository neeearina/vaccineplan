# Generated by Django 4.2 on 2023-12-21 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
        ("clinics", "0007_remove_clinics_admins_clinics_admin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinics",
            name="city",
            field=models.ForeignKey(
                default=613,
                help_text="город/населенный пункт, в котором находится клиника",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.city",
                verbose_name="город",
            ),
        ),
    ]
