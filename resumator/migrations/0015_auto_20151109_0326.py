# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumator', '0014_auto_20151109_0305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-year']},
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
