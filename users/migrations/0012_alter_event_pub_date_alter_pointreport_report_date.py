# Generated by Django 4.1.2 on 2023-06-07 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_event_event_date_alter_event_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 14, 52, 28, 414648, tzinfo=datetime.timezone.utc), verbose_name='Publish Date '),
        ),
        migrations.AlterField(
            model_name='pointreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 14, 52, 28, 415509, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Report Date'),
        ),
    ]
