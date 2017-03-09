# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_mission_exe'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='exe',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
