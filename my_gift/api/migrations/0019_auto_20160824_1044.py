# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20160824_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exe_group',
            name='exe_groupname',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
