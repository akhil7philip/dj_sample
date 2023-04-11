# Generated by Django 4.2 on 2023-04-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FallSalesModel",
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
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("end_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="SalesOneModel",
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
                ("timestamp", models.DateTimeField(blank=True, null=True)),
                ("customer_name", models.TextField(blank=True, null=True)),
                ("customer_no", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.IntegerField(default=0)),
                ("is_deleted_at", models.DateTimeField(blank=True, null=True)),
                ("index", models.IntegerField()),
                ("hash", models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Sales One Model",
                "db_table": "sales one model",
            },
        ),
        migrations.CreateModel(
            name="SalesTwoModel",
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
                ("s_no", models.TextField(blank=True, null=True)),
                ("service_id", models.TextField(blank=True, null=True)),
                ("case_creation_date", models.DateField(blank=True, null=True)),
                ("case_creation_time", models.TimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("index", models.IntegerField()),
                ("hash", models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Sales Two Model",
                "db_table": "sales two model",
            },
        ),
        migrations.CreateModel(
            name="SummerSalesModel",
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
            ],
        ),
        migrations.CreateModel(
            name="WinterSalesModel",
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
            ],
        ),
    ]