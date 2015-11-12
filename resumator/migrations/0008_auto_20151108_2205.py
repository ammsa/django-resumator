# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0007_auto_20151108_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='URL',
            new_name='link',
        ),
    ]
