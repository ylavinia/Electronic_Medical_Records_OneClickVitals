# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0011_auto_20150423_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='lab_test',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
