# Generated by Django 2.2.4 on 2019-09-01 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]