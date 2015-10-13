# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gerenciamento', '0002_auto_20151011_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('motivo', models.CharField(max_length=100)),
                ('valorDevolvido', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Encontro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tema', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('vagas', models.IntegerField(default=150)),
                ('encerrado', models.BooleanField(default=False)),
                ('valor', models.DecimalField(decimal_places=2, default=150, max_digits=10)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuariorp', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descricao', models.CharField(max_length=50)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('publica', models.BooleanField(default=False)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('encontro', models.ForeignKey(to='gerenciamento.Encontro')),
                ('usuariorp', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('encontro', models.ForeignKey(to='gerenciamento.Encontro')),
            ],
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descricao', models.CharField(max_length=255)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('inscricao', models.ForeignKey(to='gerenciamento.Inscricao')),
                ('usuariorp', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('sexo', models.CharField(default='M', choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('camisa', models.CharField(max_length=2)),
                ('coordenacao', models.BooleanField(default=False)),
                ('foto', models.FileField(upload_to=None)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_alteracao', models.DateTimeField(default=django.utils.timezone.now)),
                ('irmaos', models.ManyToManyField(to='gerenciamento.Participante', related_name='irmaos_rel_+')),
                ('orgao', models.ForeignKey(to='gerenciamento.Orgao')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantesEquipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipe', models.ForeignKey(to='gerenciamento.Equipe')),
                ('participante', models.ForeignKey(to='gerenciamento.Participante')),
                ('usuariorp', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(unique=True, max_length=50)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuariorp', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDespesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuariorp', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.AddField(
            model_name='participante',
            name='quarto',
            field=models.ForeignKey(to='gerenciamento.Quarto'),
        ),
        migrations.AddField(
            model_name='participante',
            name='usuariorp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='observacao',
            name='participante',
            field=models.ForeignKey(to='gerenciamento.Participante'),
        ),
        migrations.AddField(
            model_name='observacao',
            name='usuariorp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='participante',
            field=models.ForeignKey(to='gerenciamento.Participante'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='usuariorp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='despesa',
            name='encontro',
            field=models.ForeignKey(to='gerenciamento.Encontro'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='responsavel',
            field=models.ForeignKey(to='gerenciamento.Participante'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='tipo',
            field=models.ForeignKey(to='gerenciamento.TipoDespesa'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='usuariorp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='cancelamento',
            name='inscricao',
            field=models.ForeignKey(to='gerenciamento.Inscricao'),
        ),
        migrations.AddField(
            model_name='cancelamento',
            name='usuariorp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
    ]
