# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161022_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='coc',
            name='require_pregnant',
            field=models.BooleanField(default=False),
        ),
    ]
