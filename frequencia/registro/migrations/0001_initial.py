# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('observacao', models.TextField(blank=True, verbose_name='Observação')),
                ('tipo', models.IntegerField(choices=[(0, 'Entrada'), (1, 'Saída')], default=0, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Frequência',
                'verbose_name_plural': 'Frequências',
            },
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('descricao', models.CharField(blank=True, max_length=100, verbose_name='Descricao')),
                ('ip', models.GenericIPAddressField(unique=True, unpack_ipv4=True, verbose_name='Endereço IP')),
            ],
            options={
                'verbose_name': 'Máquina',
                'verbose_name_plural': 'Máquinas',
            },
        ),
    ]