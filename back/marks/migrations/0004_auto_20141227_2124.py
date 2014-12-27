# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0003_auto_20141227_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('result', models.IntegerField()),
                ('project', models.ForeignKey(to='marks.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mark',
            name='question',
            field=models.ForeignKey(to='marks.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to='marks.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='marks',
            field=models.ManyToManyField(related_name='project_marks_student', through='marks.Mark', to='marks.Student'),
            preserve_default=True,
        ),
    ]
