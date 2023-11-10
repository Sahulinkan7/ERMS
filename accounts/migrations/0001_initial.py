# Generated by Django 4.2.5 on 2023-11-08 16:30

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
            name="EmployeeDetail",
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
                ("empcode", models.CharField(max_length=40)),
                ("empdept", models.CharField(max_length=100, null=True)),
                ("designation", models.CharField(max_length=100, null=True)),
                ("contact", models.CharField(max_length=15, null=True)),
                ("gender", models.CharField(max_length=20, null=True)),
                ("joiningdate", models.DateField(null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
