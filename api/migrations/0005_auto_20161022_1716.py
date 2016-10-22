# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20161022_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='coc_location',
            new_name='coc_location_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='modified',
        ),
        migrations.AddField(
            model_name='event',
            name='coc_location_name',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
