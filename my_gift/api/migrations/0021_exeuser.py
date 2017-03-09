# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exeuser',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
