# Generated by Django 4.1.6 on 2023-02-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_team_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(default='no', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
