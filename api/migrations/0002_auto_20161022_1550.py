# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('phone_number', models.CharField(default=b'', max_length=255)),
                ('ssn', models.CharField(default=b'', max_length=255)),
                ('dob', models.CharField(default=b'', max_length=255)),
                ('gender', models.CharField(default=b'', max_length=255)),
                ('pregnant', models.BooleanField(default=False)),
                ('race', models.CharField(default=b'', max_length=255)),
                ('marital_status', models.CharField(default=b'', max_length=255)),
                ('number_of_children', models.IntegerField(default=0, null=True, blank=True)),
                ('veteran', models.BooleanField(default=False)),
                ('occupation', models.CharField(default=b'', max_length=255)),
                ('education', models.CharField(default=b'', max_length=255)),
                ('sex_offender', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coc_location', models.CharField(default=b'', max_length=255)),
                ('event_type', models.CharField(default=b'', max_length=255)),
                ('details', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.AddField(
            model_name='fish',
            name='health',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fish',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fish',
            name='next_step_updated_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
