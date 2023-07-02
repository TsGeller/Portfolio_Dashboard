# Generated by Django 4.2.2 on 2023-07-02 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("value_lastDay", models.DecimalField(decimal_places=2, max_digits=10)),
                ("value_today", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("ticker", models.CharField(max_length=10)),
                ("name_stock", models.CharField(max_length=200)),
                ("type_stock", models.CharField(max_length=200)),
                ("currency", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Holding",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                (
                    "sock_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.stock",
                    ),
                ),
                (
                    "wallet_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.portfolio",
                    ),
                ),
            ],
        ),
    ]
