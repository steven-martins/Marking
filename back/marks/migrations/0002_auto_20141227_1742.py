# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.ImageField(max_length=150, upload_to='picture/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pictures',
            field=models.ManyToManyField(to='marks.Picture', null=True),
        ),
    ]
