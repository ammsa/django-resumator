# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0010_auto_20151108_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='experience',
        ),
        migrations.AddField(
            model_name='language',
            name='experience',
            field=models.ManyToManyField(default=None, to='resumator.Experience', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='language',
            name='projects',
        ),
        migrations.AddField(
            model_name='language',
            name='projects',
            field=models.ManyToManyField(default=None, to='resumator.Project', null=True, blank=True),
        ),
    ]
