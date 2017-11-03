# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-03 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculo',
            name='inicio_vigencia',
            field=models.DateField(blank=True, null=True, verbose_name='Data de início da bolsa'),
        ),
        migrations.AddField(
            model_name='vinculo',
            name='termino_vigencia',
            field=models.DateField(blank=True, null=True, verbose_name='Data de término da bolsa'),
        ),
    ]