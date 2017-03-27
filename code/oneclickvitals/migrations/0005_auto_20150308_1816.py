# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0004_auto_20150308_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='newpatient',
            old_name='patient_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='newpatient',
            old_name='patient_date_of_birth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='newpatient',
            old_name='patient_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='newpatient',
            old_name='patient_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='newpatient',
            old_name='patient_phone_number',
            new_name='phone_number',
        ),
    ]
