# Generated by Django 2.2.4 on 2019-09-01 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190901_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_time_end',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Event end time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_time_start',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Event start time'),
            preserve_default=False,
        ),
    ]