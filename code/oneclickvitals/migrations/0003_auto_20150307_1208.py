# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(null=True, max_length=15),
            preserve_default=True,
        ),
    ]
