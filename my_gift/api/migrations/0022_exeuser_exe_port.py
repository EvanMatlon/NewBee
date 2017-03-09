# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_exeuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='exeuser',
            name='exe_port',
            field=models.IntegerField(default=3306),
            preserve_default=False,
        ),
    ]
