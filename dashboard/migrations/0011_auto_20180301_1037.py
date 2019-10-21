# Generated by Django 2.0.2 on 2018-03-01 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20180301_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='readers',
            field=models.ManyToManyField(related_name='news_reader', through='dashboard.Reader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reader',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]