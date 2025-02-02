# Generated by Django 4.1.2 on 2023-06-07 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_event_pub_date_alter_pointreport_report_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointreport',
            name='notes',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 18, 14, 54, 600093, tzinfo=datetime.timezone.utc), verbose_name='Publish Date '),
        ),
        migrations.AlterField(
            model_name='pointreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 18, 14, 54, 601023, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Report Date'),
        ),
    ]
