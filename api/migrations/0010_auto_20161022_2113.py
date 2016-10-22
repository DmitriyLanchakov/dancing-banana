# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_event_from_coc_location_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fish',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='from_coc_location_id',
            new_name='referred_from_coc_location_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='coc_location_name',
        ),
    ]
