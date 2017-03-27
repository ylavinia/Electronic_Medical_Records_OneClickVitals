# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0009_auto_20150317_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpatient',
            name='author',
        ),
        migrations.DeleteModel(
            name='Newpatient',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='phone_number',
        ),
    ]
