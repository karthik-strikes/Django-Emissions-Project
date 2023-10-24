# Generated by Django 4.2.6 on 2023-10-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emissions",
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
                ("date_created", models.DateField(auto_now_add=True)),
                ("accounting_period", models.CharField(max_length=255)),
                ("scope_1", models.IntegerField(null=True)),
                ("scope_2", models.IntegerField(null=True)),
                ("scope_3", models.IntegerField(null=True)),
            ],
        ),
    ]
