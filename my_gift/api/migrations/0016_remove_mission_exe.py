# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_mission_exe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='exe',
        ),
    ]
