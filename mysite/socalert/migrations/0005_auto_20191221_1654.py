# Generated by Django 2.1.15 on 2019-12-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socalert', '0004_event_alert_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_alert',
            name='is_incident',
            field=models.IntegerField(choices=[(0, 'Unaware'), (1, 'Incident'), (2, 'Event')], default=0),
        ),
    ]
