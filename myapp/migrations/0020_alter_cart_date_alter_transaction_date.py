# Generated by Django 4.2.5 on 2024-01-01 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_cart_date_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 16, 30, 42, 857414, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 16, 30, 42, 873057, tzinfo=datetime.timezone.utc)),
        ),
    ]
