# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20161022_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='middle_name',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
