# Generated by Django 4.2.5 on 2023-11-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_creator_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='chronicle',
            name='players',
            field=models.ManyToManyField(to='core.player', verbose_name='Players'),
        ),
    ]
