# Generated by Django 4.2.5 on 2023-10-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_character_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='E-mail'),
        ),
    ]
