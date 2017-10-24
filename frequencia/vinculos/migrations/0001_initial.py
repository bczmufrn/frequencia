# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenadoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Coordenadoria',
                'verbose_name_plural': 'Coordenadorias',
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('coordenadoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setores', to='vinculos.Coordenadoria', verbose_name='Coordenadoria')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('carga_horaria_diaria', models.IntegerField(blank=True, null=True, verbose_name='Carga horária diária')),
                ('turno', models.IntegerField(blank=True, choices=[(None, ''), (0, 'Matutino'), (1, 'Verpertino'), (2, 'Noturno')], null=True, verbose_name='Turno')),
                ('ativo', models.BooleanField(default=True, verbose_name='Vínculo ativo')),
                ('coordenadoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to='vinculos.Coordenadoria', verbose_name='Coordenadoria')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to='auth.Group', verbose_name='Papel')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to='vinculos.Setor', verbose_name='Setor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Vínculo',
                'verbose_name_plural': 'Vínculos',
            },
        ),
    ]
