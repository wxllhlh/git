# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ht', '0004_todo_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='a',
        ),
    ]
