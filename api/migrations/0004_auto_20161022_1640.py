# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_coc'),
    ]

    operations = [
        migrations.AddField(
            model_name='coc',
            name='beds_available',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coc',
            name='beds_total',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='client_id',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
