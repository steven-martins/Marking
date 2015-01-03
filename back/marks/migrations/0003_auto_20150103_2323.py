# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0002_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='created',
            field=models.DateTimeField(default=datetime.date(2015, 1, 3), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2015, 1, 3)),
            preserve_default=False,
        ),
    ]
