# Generated by Django 4.1.2 on 2023-06-08 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_event_pub_date_alter_pointreport_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 16, 8, 53, 35589, tzinfo=datetime.timezone.utc), verbose_name='Publish Date '),
        ),
        migrations.AlterField(
            model_name='pointreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 16, 8, 53, 36488, tzinfo=datetime.timezone.utc), verbose_name='Report Date'),
        ),
    ]
