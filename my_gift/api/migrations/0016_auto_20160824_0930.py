# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_mission_exe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
