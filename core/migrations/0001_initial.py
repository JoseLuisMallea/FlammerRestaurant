# Generated by Django 3.2.9 on 2021-11-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='idUsuario')),
                ('correo', models.CharField(max_length=50, verbose_name='correo')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
            ],
            options={
                'verbose_name': ['usuario',],
                'verbose_name_plural': ['usuarios',],
                'ordering': ['idUsuario'],
            },
        ),
    ]