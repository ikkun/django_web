# Generated by Django 3.0 on 2019-12-27 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socalert', '0009_auto_20191224_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rule', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('impact', models.IntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low')])),
                ('urgency', models.IntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low')])),
                ('contact', models.TextField(blank=True, null=True)),
                ('howto', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdby2user', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updatedby2user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]