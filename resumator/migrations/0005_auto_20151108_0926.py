# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0004_auto_20151108_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='picture',
            new_name='image',
        ),
    ]
