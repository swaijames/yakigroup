# Generated by Django 3.2.14 on 2022-10-18 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapi', '0004_auto_20221018_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 50, 24, 100762)),
        ),
        migrations.AlterField(
            model_name='destination',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 50, 24, 100762)),
        ),
        migrations.AlterField(
            model_name='package',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 50, 24, 99762)),
        ),
        migrations.AlterField(
            model_name='package',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 50, 24, 99762)),
        ),
    ]