# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0017_auto_20150428_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsigns',
            name='blood_pressure',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
