# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('doctor_id', models.IntegerField()),
                ('is_doctor', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('access_token', models.CharField(max_length=100)),
                ('refresh_token', models.CharField(max_length=100)),
            ],
        ),
    ]
