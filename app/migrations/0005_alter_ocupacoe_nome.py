# Generated by Django 5.0.3 on 2024-03-31 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ocupacoe_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocupacoe',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
