# Generated by Django 2.1.15 on 2019-12-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socalert', '0005_auto_20191221_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_alert',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
