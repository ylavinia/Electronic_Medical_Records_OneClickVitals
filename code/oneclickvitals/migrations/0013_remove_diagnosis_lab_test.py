# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0012_diagnosis_lab_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosis',
            name='lab_test',
        ),
    ]
