# Generated by Django 4.2.5 on 2023-11-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="percentagegrad",
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="percentagehsc",
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="percentagessc",
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="yearofpassinggrad",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="yearofpassinghsc",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="yearofpassingpg",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="employeeeducationdetail",
            name="yearofpassingssc",
            field=models.DateField(null=True),
        ),
    ]
