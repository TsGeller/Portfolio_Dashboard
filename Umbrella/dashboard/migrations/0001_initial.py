# Generated by Django 5.0.1 on 2024-02-01 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('value_lastDay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('value_today', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ticker', models.CharField(max_length=10)),
                ('name_stock', models.CharField(max_length=100)),
                ('type_stock', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('wallet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.portfolio')),
                ('sock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.stock')),
            ],
        ),
        migrations.CreateModel(
            name='ActorCashflow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conversion_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_eur', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('wallet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.portfolio')),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.stock')),
            ],
        ),
        migrations.CreateModel(
            name='WalletCashflow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('cashflow_entry', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.holder')),
                ('wallet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.portfolio')),
            ],
        ),
    ]
