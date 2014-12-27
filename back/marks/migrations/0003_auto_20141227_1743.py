# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0002_auto_20141227_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pictures',
            field=models.ManyToManyField(to='marks.Picture', blank=True),
        ),
    ]
