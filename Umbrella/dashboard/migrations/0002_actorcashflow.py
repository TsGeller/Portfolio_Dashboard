# Generated by Django 4.2.2 on 2023-07-02 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActorCashflow",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "conversion_rate",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("price_eur", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("charges", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                (
                    "stock_id",
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