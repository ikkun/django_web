# Generated by Django 3.0 on 2019-12-19 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socalert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_alert',
            name='severity',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')]),
        ),
    ]