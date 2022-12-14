# Generated by Django 4.1.2 on 2022-11-04 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 101848)),
        ),
        migrations.AlterField(
            model_name='destination',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 101848)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 101848)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 101848)),
        ),
        migrations.AlterField(
            model_name='hero',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 102848)),
        ),
        migrations.AlterField(
            model_name='hero',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 102848)),
        ),
        migrations.AlterField(
            model_name='package',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 102848)),
        ),
        migrations.AlterField(
            model_name='package',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 102848)),
        ),
        migrations.AlterField(
            model_name='package_data',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 102848)),
        ),
        migrations.AlterField(
            model_name='package_data',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 10, 41, 45, 102848)),
        ),
    ]
