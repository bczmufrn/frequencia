# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vinculos', '0001_initial'),
        ('justificativas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='justificativafalta',
            name='usuario_analise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='justificativas_homologadas', to='vinculos.Vinculo', verbose_name='Analisado por'),
        ),
        migrations.AddField(
            model_name='justificativafalta',
            name='vinculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='justificativas', to='vinculos.Vinculo', verbose_name='Vínculo'),
        ),
    ]
