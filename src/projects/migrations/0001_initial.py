# Generated by Django 4.1.7 on 2023-02-22 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "employees",
                    models.ManyToManyField(
                        related_name="projects",
                        to="employees.employee",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="employees.employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "project",
                "verbose_name_plural": "projects",
            },
        ),
    ]
