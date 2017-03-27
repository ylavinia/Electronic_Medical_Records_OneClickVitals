# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0007_auto_20150309_1458'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientDetails',
        ),
    ]
