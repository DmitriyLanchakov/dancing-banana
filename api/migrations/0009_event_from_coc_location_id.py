# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_coc_require_pregnant'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='from_coc_location_id',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
