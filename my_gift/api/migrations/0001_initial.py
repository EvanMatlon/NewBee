# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exe_group',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('exe_groupname', models.CharField(max_length=128)),
                ('group_var', models.CharField(max_length=256, blank=True)),
                ('detail', models.CharField(max_length=1024)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Functiongroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('fun_groupname', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hostname', models.CharField(max_length=128)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('port', models.IntegerField()),
                ('status', models.IntegerField()),
                ('host_var', models.CharField(max_length=512)),
                ('function_group', models.ForeignKey(to='api.Functiongroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Host_exe_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('exe_groupid', models.ForeignKey(to='api.Exe_group')),
                ('hostid', models.ForeignKey(to='api.Host')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('rolename', models.CharField(max_length=128)),
                ('exe_groupname', models.CharField(max_length=128)),
                ('exe', models.CharField(max_length=128)),
                ('log', models.CharField(max_length=128)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Num',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('rolename', models.CharField(max_length=128)),
                ('detail', models.CharField(max_length=1024)),
                ('stepnum', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
