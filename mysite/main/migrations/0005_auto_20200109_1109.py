# Generated by Django 3.0.2 on 2020-01-09 16:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20200108_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='league_team_owners',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_ownerID',
        ),
        migrations.AddField(
            model_name='league',
            name='league_owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='team_owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='league',
            name='league_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 11, 9, 35, 372972), verbose_name='date published'),
        ),
    ]
