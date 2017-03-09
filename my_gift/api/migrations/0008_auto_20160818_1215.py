# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160818_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='exeid',
            new_name='exe',
        ),
        migrations.RenameField(
            model_name='mission',
            old_name='rolename',
            new_name='rolenameid',
        ),
    ]
