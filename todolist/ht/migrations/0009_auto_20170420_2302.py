# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ht', '0008_todo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['modifytime']},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='datatime',
            new_name='modifytime',
        ),
    ]
