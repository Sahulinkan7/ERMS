# Generated by Django 4.2.5 on 2023-11-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0002_alter_employeeeducationdetail_percentagegrad_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="percentagepg",
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]