# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_mission_exe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='exe_groupnameid',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='rolenameid',
        ),
        migrations.AddField(
            model_name='mission',
            name='exe_groupname',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mission',
            name='rolename',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
