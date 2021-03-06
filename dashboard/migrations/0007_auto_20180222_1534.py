# Generated by Django 2.0.2 on 2018-02-22 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='close_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='change',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='change',
            name='unavailability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='change',
            name='validate',
            field=models.BooleanField(default=False),
        ),
    ]
