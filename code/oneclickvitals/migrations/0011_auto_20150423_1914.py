# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0010_auto_20150317_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('diagnosis_date', models.DateField(default=django.utils.timezone.now)),
                ('complaint', models.TextField(max_length=500)),
                ('diagnosis', models.TextField(max_length=1000)),
                ('additional_comments', models.TextField(max_length=500)),
                ('follow_up', models.NullBooleanField()),
                ('patient', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DoctorDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('doctor_first_name', models.CharField(default='Victor', max_length=50)),
                ('doctor_last_name', models.CharField(default='Vitals', max_length=50)),
                ('name_suffix', models.CharField(default='M.D.', max_length=10)),
                ('license_number', models.CharField(default='A8039V92', max_length=8)),
                ('prescription_network_id', models.CharField(default='8841038281943', max_length=13)),
                ('dea', models.CharField(default='83059667', max_length=8)),
                ('doctor_phone_number', models.CharField(default='(717) 444-0880', max_length=14)),
                ('address_1', models.CharField(default='Grand Pasteur Clinic', max_length=128, verbose_name='address')),
                ('address_2', models.CharField(default='515 Hamilton Ave', max_length=128, verbose_name="address cont'd")),
                ('city', models.CharField(default='Fullerton', max_length=64, verbose_name='city')),
                ('state', localflavor.us.models.USStateField(default='CA', max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], verbose_name='state')),
                ('zip_code', models.CharField(default='92652', max_length=5, verbose_name='zip code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('contact_first_name', models.CharField(max_length=50, null=True)),
                ('contact_last_name', models.CharField(max_length=50, null=True)),
                ('relationship', models.CharField(max_length=50, choices=[('Spouse', 'spouse'), ('Parent', 'parent'), ('Brother', 'brother'), ('Sister', 'sister'), ('Boyfriend', 'boyfriend'), ('Girlfriend', 'girlfriend'), ('Other', 'other')], null=True)),
                ('contact_phone_number', models.CharField(max_length=10, null=True)),
                ('address_1', models.CharField(max_length=128, verbose_name='address', blank=True)),
                ('address_2', models.CharField(max_length=128, verbose_name="address cont'd", blank=True)),
                ('city', models.CharField(default='Fullerton', max_length=64, verbose_name='city')),
                ('state', localflavor.us.models.USStateField(default='CA', max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], verbose_name='state')),
                ('zip_code', models.CharField(default='92614', max_length=5, verbose_name='zip code')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FamilyMedicalHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('stroke', models.NullBooleanField()),
                ('cancer', models.NullBooleanField()),
                ('high_bp', models.NullBooleanField()),
                ('tuberculosis', models.NullBooleanField()),
                ('diabetes', models.NullBooleanField()),
                ('leukemia', models.NullBooleanField()),
                ('bleeding_tendency', models.NullBooleanField()),
                ('heart_attack', models.NullBooleanField()),
                ('kidney_disease', models.NullBooleanField()),
                ('rheumatic_heart', models.NullBooleanField()),
                ('heart_failure', models.NullBooleanField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('urine_culture', models.NullBooleanField()),
                ('blood_culture', models.NullBooleanField()),
                ('allergy_test', models.NullBooleanField()),
                ('blood_glucose', models.NullBooleanField()),
                ('thyroid', models.NullBooleanField()),
                ('viral_test', models.NullBooleanField()),
                ('pregnancy_test', models.NullBooleanField()),
                ('x_ray', models.CharField(choices=[('finger', 'Finger'), ('palm', 'Palm'), ('wrist', 'Wrist'), ('right elbow', 'Right Elbow'), ('left elbow', 'Left Elbow'), ('right shoulder', 'Right Shoulder'), ('neck', 'Neck'), ('upper back', 'Upper Back'), ('middle back', 'Middle Back'), ('lower back', 'Lower Back'), ('right knee', 'Right Knee'), ('left knee', 'Left Knee'), ('right leg', 'Right leg'), ('left leg', 'Left Leg'), ('right ankle', 'Right Ankle'), ('left ankle', 'Left Ankle'), ('right foot', 'Right Foot'), ('left foot', 'Left Foot'), ('other', 'Other'), ('none', 'None')], max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatientMedicalHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('height', models.PositiveIntegerField(max_length=5, null=True)),
                ('weight', models.FloatField(max_length=10, null=True)),
                ('blood_type', models.CharField(max_length=4, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], null=True)),
                ('allergies', models.TextField(max_length=100)),
                ('current_medications', models.TextField(max_length=500)),
                ('chief_complaint', models.TextField(max_length=500, null=True)),
                ('surgical_history', models.TextField(max_length=500)),
                ('medical_history', models.TextField(max_length=500)),
                ('social_habits', models.CharField(choices=[('Smoking', 'smoking'), ('Alcohol', 'alcohol'), ('Exercise', 'exercise'), ('Street drugs', 'street drugs'), ('Other', 'other'), ('None', 'none')], max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PharmacyDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pharmacy_name', models.CharField(max_length=50, null=True)),
                ('address_1', models.CharField(max_length=128, verbose_name='address', blank=True)),
                ('address_2', models.CharField(max_length=128, verbose_name="address cont'd", blank=True)),
                ('city', models.CharField(default='Fullerton', max_length=64, verbose_name='city')),
                ('pharmacy_phone_number', models.CharField(max_length=14, null=True)),
                ('state', localflavor.us.models.USStateField(default='CA', max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], verbose_name='state')),
                ('zip_code', models.CharField(default='92614', max_length=5, verbose_name='zip code')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('gender', models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True)),
                ('date_of_issuance', models.CharField(max_length=10, null=True)),
                ('days_supply', models.CharField(max_length=5, null=True, blank=True)),
                ('drug_name', models.CharField(max_length=100, null=True, blank=True)),
                ('drug_strength', models.CharField(max_length=5, null=True, blank=True)),
                ('dosage_form', models.CharField(max_length=20, null=True, blank=True)),
                ('frequency', models.CharField(choices=[('Daily', 'daily'), ('Every Other Day', 'every other day'), ('Twice a Day', 'BID/b.i.d.'), ('Three Times a Day', 'TID/t.id'), ('Four Times a Day', 'QID/q.i.d.'), ('Every Bedtime', 'QHS'), ('Every 4 Hours', 'Q4h'), ('Every 4 to 6 Hours', 'Q4-6h'), ('Every Week', 'QWK')], max_length=50)),
                ('quantity', models.CharField(max_length=6, null=True, blank=True)),
                ('npi_number', models.CharField(max_length=10)),
                ('ndc_number', models.CharField(max_length=11)),
                ('refills', models.NullBooleanField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Radiology',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60, blank=True)),
                ('image', models.ImageField(upload_to='image')),
                ('created_date', models.DateField(null=True, blank=True)),
                ('caption', models.CharField(max_length=60, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VitalSigns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('visit_date', models.DateField(default=django.utils.timezone.now)),
                ('heart_rate', models.CharField(max_length=5)),
                ('blood_pressure', models.CharField(max_length=5)),
                ('temperature', models.CharField(max_length=5)),
                ('current_weight', models.CharField(max_length=5)),
                ('current_height', models.CharField(max_length=5)),
                ('notes', models.TextField(max_length=500, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='reason',
            new_name='reason_for_appointment',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='address',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='type_of_appointment',
            field=models.CharField(max_length=100, choices=[('Routine Preventive Care', 'Routine Preventive Care'), ('Follow-Up', 'Follow-Up'), ('Routine Problem Visit', 'Routine Problem Visit'), ('Urgent/Same Day Appointment', 'Urgent/Same Day Appointment'), ('Nurse Visit', 'Nurse Visit'), ('Allergy Shots', 'Allergy Shots'), ('New Patients and Referrals', 'New Patients and Referrals')], null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='address_1',
            field=models.CharField(max_length=128, verbose_name='address', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='address_2',
            field=models.CharField(max_length=128, verbose_name="address cont'd", blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='gender',
            field=models.CharField(max_length=50, choices=[('Female', 'female'), ('Male', 'male')], null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='insurance',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='state',
            field=localflavor.us.models.USStateField(default='CA', max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='zip_code',
            field=models.CharField(default='92614', max_length=5, verbose_name='zip code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='city',
            field=models.CharField(default='Fullerton', max_length=64, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
    ]
