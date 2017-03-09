# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_role_stepnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='stepnum',
            field=models.IntegerField(default=1),
        ),
    ]
