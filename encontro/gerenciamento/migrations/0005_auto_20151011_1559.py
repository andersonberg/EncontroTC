# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0004_auto_20151011_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantesequipe',
            name='equipe',
        ),
        migrations.RemoveField(
            model_name='participantesequipe',
            name='participante',
        ),
        migrations.RemoveField(
            model_name='participantesequipe',
            name='usuariorp',
        ),
        migrations.AddField(
            model_name='equipe',
            name='membros',
            field=models.ManyToManyField(to='gerenciamento.Participante'),
        ),
        migrations.DeleteModel(
            name='ParticipantesEquipe',
        ),
    ]
