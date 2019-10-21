# Generated by Django 2.0.2 on 2018-02-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20180220_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=400)),
                ('ticket', models.IntegerField()),
                ('uol', models.CharField(blank=True, max_length=20)),
                ('rdm', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Change',
                'verbose_name_plural': 'Change',
                'ordering': ('created',),
            },
        ),
    ]