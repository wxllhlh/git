# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ht', '0006_min'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Min',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
