# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20160824_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functiongroup',
            name='fun_groupname',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
