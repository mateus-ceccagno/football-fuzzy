# Generated by Django 4.1.3 on 2022-12-05 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nflscoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='resultado',
            field=models.FloatField(),
        ),
    ]