from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
from django.core.urlresolvers import reverse
from django.core.files import File
from os.path import join as pjoin
from tempfile import *
from PIL import Image as PImage




from django.utils.translation import ugettext as _

from localflavor.us.models import USStateField

class Appointment(models.Model):

    user = models.ForeignKey(User) 
    APPOINTMENT_CHOICES = (('Routine Preventive Care', 'Routine Preventive Care',),
                            ('Follow-Up', 'Follow-Up',),
                            ('Routine Problem Visit', 'Routine Problem Visit'),
                            ('Urgent/Same Day Appointment', 'Urgent/Same Day Appointment'),
                            ('Nurse Visit', 'Nurse Visit'),
                            ('Allergy Shots', 'Allergy Shots'),
                            ('New Patients and Referrals', 'New Patients and Referrals'),)

    type_of_appointment = models.CharField(max_length=100, choices=APPOINTMENT_CHOICES, null = True)
    reason_for_appointment = models.CharField(max_length=50, null = True)
    phone_number = models.CharField(max_length=14, null = True)
    
    appointment_date = models.DateField(
            blank=True, null=True)
    appointment_time = models.TimeField(
            blank=True, null=True)
    #cancel = models.NullBooleanField()

    def __str__(self):
        return self.user.username

class PageAdmin(admin.ModelAdmin):

    list_display = ('last_name', 'phone_number')

    def __str__(self):
        return self.list_display

class UserDetail(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    GENDER_CHOICES = (( 'Female','female',), ('Male', 'male',))
    # The additional attributes we wish to include.

    phone_number = models.CharField(max_length=14, null = True)
    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")

    #state = USStateField(choices = STATE_CHOICES, default="CA" )

    zip_code = models.CharField(_("zip code"), max_length=5, default= '92614')
    insurance = models.CharField(max_length=50, null = True)
    date_of_birth = models.CharField(max_length=10, null = True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null = True)

   

    def __str__(self):
        return self.user.username


class EmergencyContact(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    RELATIONSHIP_CHOICES =  (('Spouse','spouse',), ('Parent', 'parent',), ('Daughter', 'daughter'), ('Son', 'son'), ('Brother', 'brother'),('Sister', 'sister'), ('Boyfriend', 'boyfriend'), ('Girlfriend', 'girlfriend'), ('Other', 'other'),)

    # The additional attributes we wish to include.
    contact_first_name = models.CharField(max_length=50, null = True)
    contact_last_name = models.CharField(max_length=50, null = True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES, null = True)

    contact_phone_number = models.CharField(max_length=14, null = True)

    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92614')


    def __str__(self):
        return self.user.username

class PatientMedicalHistory(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    HABIT_CHOICES = (('Smoking', 'smoking'),('Alcohol', 'alcohol'),('Exercise', 'exercise'),
                        ('Street drugs', 'street drugs'),('Other', 'other'),('None', 'none'))
    # The additional attributes we wish to include.
    height = models.PositiveIntegerField(max_length=5, null = True)
    weight = models.FloatField(max_length=10, null = True)
    BLOOD_TYPE_CHOICES = (('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-'))
    blood_type = models.CharField(max_length=4, choices=BLOOD_TYPE_CHOICES, null=True)
    allergies = models.TextField(max_length=100)
    current_medications = models.TextField(max_length=500)
    chief_complaint = models.TextField(max_length=500, null=True)

    surgical_history = models.TextField(max_length=500)
    medical_history = models.TextField(max_length=500)
    social_habits = models.CharField(max_length=50, choices=HABIT_CHOICES)


    def __str__(self):
        return self.user.username


class FamilyMedicalHistory(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    stroke = models.NullBooleanField()
    cancer = models.NullBooleanField()
    high_bp = models.NullBooleanField()
    tuberculosis = models.NullBooleanField()
    diabetes = models.NullBooleanField()
    leukemia = models.NullBooleanField()
    bleeding_tendency = models.NullBooleanField()
    heart_attack = models.NullBooleanField()
    kidney_disease = models.NullBooleanField()
    rheumatic_heart = models.NullBooleanField()
    heart_failure = models.NullBooleanField()


    def __str__(self):
        return self.user.username


    
class VitalSigns(models.Model):
    user = models.ForeignKey(User)
    visit_date = models.DateField(default=timezone.now)
    heart_rate = models.CharField(max_length=5)
    blood_pressure = models.CharField(max_length=6)
    temperature = models.CharField(max_length=5)
    current_weight = models.CharField(max_length=5)
    current_height = models.CharField(max_length=5)
    notes = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Diagnosis(models.Model):
    
    patient = models.ForeignKey(User, null=True)
    diagnosis_date = models.DateField(blank=True, null=True)
    complaint = models.TextField(max_length=500)
    diagnosis = models.TextField(max_length=1000)
    additional_comments = models.TextField(max_length=500)
    follow_up = models.NullBooleanField()
    
    def __str__(self):
        return self.diagnosis
    

class LabTest(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User)
    XRAY_CHOICES = (('finger', 'Finger'),('palm', 'Palm'),('wrist', 'Wrist'),
                    ('right elbow', 'Right Elbow'),('left elbow', 'Left Elbow'),
                    ('right shoulder', 'Right Shoulder'),('neck', 'Neck'),('upper back', 'Upper Back'),
                    ('middle back', 'Middle Back'),('lower back', 'Lower Back'),
                    ('right knee', 'Right Knee'),('left knee', 'Left Knee'),
                    ('right leg', 'Right leg'),('left leg', 'Left Leg'),
                    ('right ankle', 'Right Ankle'), ('left ankle', 'Left Ankle'),
                    ('right foot', 'Right Foot'),('left foot', 'Left Foot'),('left shoulder', 'Left Shoulder'),('lungs', 'Lungs'), ('head','Head'), ('other', 'Other'), ('none', 'None'),)
    test_date = models.DateField(blank=True, null=True)
    # The additional attributes we wish to include.
    urine_culture = models.NullBooleanField()
    blood_culture = models.NullBooleanField()
    allergy_test = models.NullBooleanField()
    blood_glucose = models.NullBooleanField()
    thyroid = models.NullBooleanField()
    viral_test = models.NullBooleanField()
    pregnancy_test = models.NullBooleanField()
    x_ray = models.CharField(max_length=50, choices=XRAY_CHOICES)


    def __str__(self):
        return self.user.username

    
class Radiology(models.Model):   

    user = models.ForeignKey(User)
    title = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='image')
    created_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=60, blank=True)


    def __str__(self):
        return self.user.last_name

class DoctorDetail(models.Model):
    # This line is required. Links UserProfile to a User model instance.

    
    doctor_first_name = models.CharField(max_length=50, default="Victor")
    doctor_last_name = models.CharField(max_length=50, default="Vitals")
    name_suffix = models.CharField(max_length=10, default="M.D.")
    license_number = models.CharField(max_length=8,default='A8039V92' )
    prescription_network_id = models.CharField(max_length=13, default='8841038281943')
    dea = models.CharField(max_length=8, default='83059667')
    doctor_phone_number = models.CharField(max_length=14, default='(717) 444-0880')

    address_1 = models.CharField(_("address"), max_length=128, default="Grand Pasteur Clinic")
    address_2 = models.CharField(_("address cont'd"), max_length=128, default="515 Hamilton Ave")
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92652')

    def __str__(self):
        return self.doctor_last_name

class PharmacyDetail(models.Model):

    user = models.OneToOneField(User, null=True)
    pharmacy_name = models.CharField(max_length=50, null=True)
    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    pharmacy_phone_number = models.CharField(max_length=14, null=True)
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92614')
    
    def __str__(self):
        return self.user.username
    


class Prescription(models.Model):
    #DEFAULT_PK=1
    user = models.ForeignKey(User)
    FREQUENCY_CHOICES = (('daily','Daily',),('every other day','Every Other Day',),('Twice a Day','BID/b.i.d.',),('Three Times a Day','TID/t.id',), ('Four Times a Day','QID/q.i.d.',), ('Every Bedtime','QHS',), ('Every 4 Hours','Q4h',), ('Every 4 to 6 Hours','Q4-6h',), ('Every Week','QWK',),)
    GENDER_CHOICES = (('male','Male'), ('female', 'Female'))
    #REFILLS_CHOICES = (('yes', 'Yes',), ('no', 'No',),)
    #patient = models.ForeignKey('auth.User')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    ROUTE_CHOICES = (('po (by mouth)', 'PO (by mouth)'), ('pr (per rectum)', 'PR (per rectum)'),
                     ('im (intramuscular)', 'IM (intramuscular)'), ('iv (intravenous)', 'IV (intravenous)'),
                     ('id (intradermal)', 'ID (intradermal)'), ('in (intranasal)','IN (intranasal)'),
                     ('tp (topical)', 'TP (topical)'))
    date_of_issuance = models.CharField(max_length=10, null = True)

    days_supply = models.CharField(max_length=5, blank=True, null=True)
    drug_name = models.CharField(max_length=100, blank=True, null=True)
    drug_strength = models.CharField(max_length=5, blank=True, null=True)
    dosage_form = models.CharField(max_length=20, choices=ROUTE_CHOICES, null=True)

    FREQUENCY_CHOICES = (('Daily','daily',),('Every Other Day','every other day',),('Twice a Day','BID/b.i.d.',),('Three Times a Day','TID/t.id',), ('Four Times a Day','QID/q.i.d.',), ('Every Bedtime','QHS',), ('Every 4 Hours','Q4h',), ('Every 4 to 6 Hours','Q4-6h',), ('Every Week','QWK',),)

    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    quantity = models.CharField(max_length=6, blank=True, null=True)
    npi_number = models.CharField(max_length=10)
    ndc_number = models.CharField(max_length=11)
    refills = models.NullBooleanField()

    
    def __str__(self):
        return self.drug_name
    

class LabResults(models.Model):
    user = models.ForeignKey(User)
    TEST_CHOICES = (('urine culture', 'Urine Culture'), ('blood culture', 'Blood Culture'),
                    ('allergy test', 'Allergy Test'), ('blood glucose', 'Blood Glucose'),
                    ('thyroid', 'Thyroid'), ('pregnancy test', 'Pregnancy Test'),)
    RESULT_CHOICES = (('positive', 'Positive'), ('negative', 'Negative'))
    test_date = models.DateField(blank=True, null=True)
    test_type = models.CharField(max_length=50, choices=TEST_CHOICES, null = True)
    specific_gravity = models.FloatField(max_length=6, null = True)
    pH = models.FloatField(max_length=4, null = True)
    protein = models.PositiveIntegerField(max_length=3, null = True)
    glucose = models.PositiveIntegerField(max_length=3, null = True)
    ketones = models.CharField(max_length=50, choices=RESULT_CHOICES, null = True)
    blood = models.CharField(max_length=50, choices=RESULT_CHOICES, null = True)
    leukocyte_esterase = models.CharField(max_length=50, choices=RESULT_CHOICES, null = True)
    nitrite = models.CharField(max_length=50, choices=RESULT_CHOICES, null = True)
    bilirubin = models.CharField(max_length=50, choices=RESULT_CHOICES, null = True)
    urobilinogen = models.CharField(max_length=50, choices=RESULT_CHOICES, null = True)

    def __str__(self):
        return self.user.username




