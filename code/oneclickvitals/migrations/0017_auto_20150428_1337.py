# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0016_auto_20150428_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('test_type', models.CharField(choices=[('urine culture', 'Urine Culture'), ('blood culture', 'Blood Culture'), ('allergy test', 'Allergy Test'), ('blood glucose', 'Blood Glucose'), ('thyroid', 'Thyroid'), ('pregnancy test', 'Pregnancy Test')], max_length=50, null=True)),
                ('specific_gravity', models.FloatField(max_length=6, null=True)),
                ('pH', models.FloatField(max_length=4, null=True)),
                ('protein', models.PositiveIntegerField(max_length=3, null=True)),
                ('glucose', models.PositiveIntegerField(max_length=3, null=True)),
                ('ketones', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50, null=True)),
                ('blood', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50, null=True)),
                ('leukocyte_esterase', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50, null=True)),
                ('nitrite', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50, null=True)),
                ('bilirubin', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50, null=True)),
                ('urobilinogen', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=50, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='labtest',
            name='test_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
