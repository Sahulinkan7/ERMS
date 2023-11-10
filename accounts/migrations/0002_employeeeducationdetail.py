# Generated by Django 4.2.5 on 2023-11-09 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeEducationDetail",
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
                ("coursepg", models.CharField(max_length=100, null=True)),
                ("institutepg", models.CharField(max_length=200, null=True)),
                ("yearofpassingpg", models.DateField()),
                ("percentagepg", models.DecimalField(decimal_places=2, max_digits=5)),
                ("coursegrad", models.CharField(max_length=100, null=True)),
                ("institutegrad", models.CharField(max_length=200, null=True)),
                ("yearofpassinggrad", models.DateField()),
                ("percentagegrad", models.DecimalField(decimal_places=2, max_digits=5)),
                ("coursessc", models.CharField(max_length=100, null=True)),
                ("institutessc", models.CharField(max_length=200, null=True)),
                ("yearofpassingssc", models.DateField()),
                ("percentagessc", models.DecimalField(decimal_places=2, max_digits=5)),
                ("coursehsc", models.CharField(max_length=100, null=True)),
                ("institutehsc", models.CharField(max_length=200, null=True)),
                ("yearofpassinghsc", models.DateField()),
                ("percentagehsc", models.DecimalField(decimal_places=2, max_digits=5)),
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