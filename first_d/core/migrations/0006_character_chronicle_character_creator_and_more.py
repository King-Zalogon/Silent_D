# Generated by Django 4.2.5 on 2023-11-03 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_chronicle_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='chronicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.chronicle'),
        ),
        migrations.AddField(
            model_name='character',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.creator'),
        ),
        migrations.AddField(
            model_name='character',
            name='rules_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.rulessystem'),
        ),
        migrations.AddField(
            model_name='chronicle',
            name='rules_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.rulessystem'),
        ),
    ]
