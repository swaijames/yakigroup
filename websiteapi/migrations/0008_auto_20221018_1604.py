# Generated by Django 3.2.14 on 2022-10-18 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapi', '0007_auto_20221018_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 16, 4, 26, 97029)),
        ),
        migrations.AlterField(
            model_name='destination',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 16, 4, 26, 97029)),
        ),
        migrations.AlterField(
            model_name='package',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 16, 4, 26, 96030)),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='package',
            name='info_detail',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='package',
            name='info_image1',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='package',
            name='info_image2',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_people_group',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_tour_guide',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='package',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 16, 4, 26, 96030)),
        ),
    ]
