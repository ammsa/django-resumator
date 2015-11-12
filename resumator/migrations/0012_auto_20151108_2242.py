# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0011_auto_20151108_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
