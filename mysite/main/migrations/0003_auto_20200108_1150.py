# Generated by Django 3.0.2 on 2020-01-08 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191223_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('team_ownerID', models.CharField(max_length=50)),
                ('adc', models.CharField(max_length=50)),
                ('jng', models.CharField(max_length=50)),
                ('mid', models.CharField(max_length=50)),
                ('bot', models.CharField(max_length=50)),
                ('sup', models.CharField(max_length=50)),
                ('flex', models.CharField(max_length=50)),
                ('bn1', models.CharField(max_length=50)),
                ('bn2', models.CharField(max_length=50)),
                ('bn3', models.CharField(max_length=50)),
                ('wins', models.CharField(max_length=50)),
                ('loss', models.CharField(max_length=50)),
                ('tie', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 8, 11, 50, 24, 141799), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=50)),
                ('league_player_size', models.CharField(max_length=50)),
                ('league_team_owners', models.CharField(max_length=50)),
                ('league_teams', models.ManyToManyField(to='main.Team')),
            ],
        ),
    ]
