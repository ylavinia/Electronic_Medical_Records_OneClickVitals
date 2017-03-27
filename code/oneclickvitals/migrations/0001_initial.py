# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('patient_first_name', models.CharField(max_length=15, null=True)),
                ('patient_last_name', models.CharField(max_length=15, null=True)),
                ('patient_phone_number', models.CharField(max_length=10, null=True)),
                ('reason', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('appointment_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Newpatient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('patient_first_name', models.CharField(max_length=15, null=True)),
                ('patient_last_name', models.CharField(max_length=15, null=True)),
                ('patient_phone_number', models.CharField(max_length=10, null=True)),
                ('patient_date_of_birth', models.DateField(max_length=8)),
                ('patient_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
