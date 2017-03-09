# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_role_stepnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='role_var',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
