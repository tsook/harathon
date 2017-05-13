# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('giver', models.CharField(max_length=50)),
                ('receiver', models.CharField(max_length=50)),
                ('money', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='user',
        ),
        migrations.DeleteModel(
            name='user_data',
        ),
    ]
