# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20161022_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='coc',
            name='allow_family',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coc',
            name='allow_single_men',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coc',
            name='allow_single_women',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coc',
            name='allow_veteran',
            field=models.BooleanField(default=False),
        ),
    ]
