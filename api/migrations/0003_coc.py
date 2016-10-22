# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161022_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('address', models.CharField(default=b'', max_length=255)),
                ('latitude', models.CharField(default=b'', max_length=255)),
                ('longitude', models.CharField(default=b'', max_length=255)),
                ('phone_number', models.CharField(default=b'', max_length=255)),
                ('coc_type', models.CharField(default=b'', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Coc',
                'verbose_name_plural': 'Cocs',
            },
        ),
    ]
