# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0014_auto_20150427_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='created_date',
        ),
    ]
