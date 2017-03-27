# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0013_remove_diagnosis_lab_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radiology',
            old_name='caption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='contact_phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
    ]
