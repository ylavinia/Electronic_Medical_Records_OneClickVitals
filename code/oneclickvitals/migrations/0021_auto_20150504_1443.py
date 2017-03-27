# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0020_auto_20150501_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(null=True, choices=[('Spouse', 'spouse'), ('Parent', 'parent'), ('Daughter', 'daughter'), ('Son', 'son'), ('Brother', 'brother'), ('Sister', 'sister'), ('Boyfriend', 'boyfriend'), ('Girlfriend', 'girlfriend'), ('Other', 'other')], max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labtest',
            name='x_ray',
            field=models.CharField(choices=[('finger', 'Finger'), ('palm', 'Palm'), ('wrist', 'Wrist'), ('right elbow', 'Right Elbow'), ('left elbow', 'Left Elbow'), ('right shoulder', 'Right Shoulder'), ('neck', 'Neck'), ('upper back', 'Upper Back'), ('middle back', 'Middle Back'), ('lower back', 'Lower Back'), ('right knee', 'Right Knee'), ('left knee', 'Left Knee'), ('right leg', 'Right leg'), ('left leg', 'Left Leg'), ('right ankle', 'Right Ankle'), ('left ankle', 'Left Ankle'), ('right foot', 'Right Foot'), ('left foot', 'Left Foot'), ('left shoulder', 'Left Shoulder'), ('lungs', 'Lungs'), ('head', 'Head'), ('other', 'Other'), ('none', 'None')], max_length=50),
            preserve_default=True,
        ),
    ]
