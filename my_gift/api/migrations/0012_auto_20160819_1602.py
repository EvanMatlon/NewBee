# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20160818_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='exe',
        ),
        migrations.AlterField(
            model_name='exe_group',
            name='detail',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
