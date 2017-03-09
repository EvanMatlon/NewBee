# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='exe',
            new_name='exeid',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='exe_groupname',
        ),
        migrations.AddField(
            model_name='mission',
            name='exe_groupnameid',
            field=models.ForeignKey(default=1, to='api.Exe_group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mission',
            name='rolename',
            field=models.ForeignKey(to='api.Role'),
        ),
    ]
