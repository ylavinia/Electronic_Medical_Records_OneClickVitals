# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0005_auto_20150308_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
