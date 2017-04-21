# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ht', '0007_auto_20170420_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('datatime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
