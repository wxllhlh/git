# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ht', '0003_auto_20170420_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='a',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
