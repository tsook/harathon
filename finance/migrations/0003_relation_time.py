# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20170513_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
