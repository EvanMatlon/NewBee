# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20160824_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='rolename',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
