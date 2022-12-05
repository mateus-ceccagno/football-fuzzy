# Generated by Django 4.1.3 on 2022-12-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('vitorias', models.IntegerField()),
                ('touchdowns', models.IntegerField()),
                ('jardas', models.IntegerField()),
                ('recepcoes', models.IntegerField()),
                ('resultado', models.FloatField())
            ],
        ),
    ]
