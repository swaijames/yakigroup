# Generated by Django 4.1.2 on 2022-10-27 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapi', '0019_alter_destination_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 14, 45, 45, 833740)),
        ),
        migrations.AlterField(
            model_name='destination',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 14, 45, 45, 833740)),
        ),
        migrations.AlterField(
            model_name='package',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 14, 45, 45, 832739)),
        ),
        migrations.AlterField(
            model_name='package',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 14, 45, 45, 832739)),
        ),
    ]