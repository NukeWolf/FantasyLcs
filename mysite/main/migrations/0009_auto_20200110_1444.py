# Generated by Django 3.0.2 on 2020-01-10 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200110_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 14, 44, 20, 299384), verbose_name='date published'),
        ),
    ]
