# Generated by Django 4.1.6 on 2023-02-07 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='photo',
        ),
    ]
