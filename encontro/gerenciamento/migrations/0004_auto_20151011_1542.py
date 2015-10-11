# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_auto_20151011_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancelamento',
            old_name='valorDevolvido',
            new_name='valor_devolvido',
        ),
    ]
