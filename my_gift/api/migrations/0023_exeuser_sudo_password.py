# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_exeuser_exe_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='exeuser',
            name='sudo_password',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
