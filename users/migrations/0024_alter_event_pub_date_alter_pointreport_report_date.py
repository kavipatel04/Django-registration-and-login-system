# Generated by Django 4.1.2 on 2023-06-08 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_event_description_event_event_s_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 16, 13, 17, 35865, tzinfo=datetime.timezone.utc), verbose_name='Publish Date '),
        ),
        migrations.AlterField(
            model_name='pointreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 16, 13, 17, 36781, tzinfo=datetime.timezone.utc), verbose_name='Report Date'),
        ),
    ]
