# Generated by Django 4.2.5 on 2023-11-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0004_employeeexperience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeexperience",
            name="company1name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
