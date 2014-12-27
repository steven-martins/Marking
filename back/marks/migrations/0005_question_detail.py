# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_auto_20141227_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='detail',
            field=models.CharField(max_length=250, blank=True, default=''),
            preserve_default=False,
        ),
    ]
