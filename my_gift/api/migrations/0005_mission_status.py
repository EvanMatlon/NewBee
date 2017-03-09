# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_mission_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
