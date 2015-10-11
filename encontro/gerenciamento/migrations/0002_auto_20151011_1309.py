# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gerenciamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='data_registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='equipe',
            name='usuariorp',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orgao',
            name='data_registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orgao',
            name='usuariorp',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
