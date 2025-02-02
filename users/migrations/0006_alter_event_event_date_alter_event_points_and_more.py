# Generated by Django 4.1.2 on 2023-06-07 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_event_profile_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(null=True, verbose_name='event date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='points',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
