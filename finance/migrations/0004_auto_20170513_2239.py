# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0003_relation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('bio', models.TextField(max_length=500, blank=True)),
                ('location', models.CharField(max_length=30, blank=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='relation',
            name='giver',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='relation',
            name='receiver',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='relation',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
