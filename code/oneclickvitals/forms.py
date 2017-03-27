from django import forms
from django.contrib.auth.models import User, Group

from oneclickvitals.models import *
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
from django.utils.safestring import mark_safe
from django.forms import Form

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email',)



class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail


        fields = ('gender','date_of_birth','insurance','phone_number','address_1','address_2','city','state','zip_code',)



class NewPatientForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('first_name','last_name','username','email', 'groups',)

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        widgets = {'appointment_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                  'appointment_time': TimeWidget(attrs= {'id':"yourtimeid"}, usel10n = True, bootstrap_version=3)}

        
        fields = ('user','type_of_appointment', 'reason_for_appointment', 'phone_number','appointment_date','appointment_time',)

class EmergencyContactForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = EmergencyContact
        fields = ('contact_first_name','contact_last_name','relationship', 'contact_phone_number','address_1','address_2','city','state','zip_code',)

class PatientMedicalHistoryForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = PatientMedicalHistory
        fields = ('height', 'weight', 'blood_type', 'allergies', 'current_medications', 'chief_complaint', 'surgical_history', 'medical_history','social_habits',)
        
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class FamilyMedicalHistoryForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = FamilyMedicalHistory
        widgets = {'stroke': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'cancer': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'high_bp': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'tuberculosis': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'diabetes': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'leukemia': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'bleeding_tendency': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'heart_attack': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'kidney_disease': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'rheumatic_heart': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'heart_failure': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    }
        fields = ('stroke','cancer','high_bp', 'tuberculosis', 'diabetes', 'leukemia', 'bleeding_tendency', 'heart_attack','kidney_disease', 'rheumatic_heart', 'heart_failure',)


class DiagnosisForm(forms.ModelForm):

    #appointment_date = forms.DateTimeField(widget = DateTimeWidget(usel10n = True, bootstrap_version = 3))
    class Meta:
        model = Diagnosis
        widgets = {'diagnosis_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                    'follow_up': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}


        fields = ('patient', 'diagnosis_date','complaint', 'diagnosis','additional_comments','follow_up',)



class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        widgets = {'test_date': DateWidget(attrs={'id':"testdate_id"}, usel10n = True, bootstrap_version=3), 
                   'urine_culture': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'blood_culture': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'blood_glucose': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'allergy_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'thyroid': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'viral_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'pregnancy_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ('user','test_date','urine_culture', 'blood_culture', 'blood_glucose', 'allergy_test', 'thyroid', 'viral_test', 'pregnancy_test', 'x_ray',)

        
class VitalSignsForm(forms.ModelForm):
    class Meta:
        model = VitalSigns
        widgets = {'visit_date': DateWidget(attrs={'id':"vitalsigns_id"}, usel10n = True, bootstrap_version=3)}
        fields = ('user','visit_date','heart_rate','blood_pressure','temperature','current_weight','current_height','notes',)
        


class PatientRadiologyImageForm(forms.ModelForm):

    class Meta:
        model = Radiology
        widgets = {'created_date': DateWidget(attrs={'id':"yourcreateddateid"}, usel10n = True, bootstrap_version=3)}
        fields = ('user', 'title', 'created_date', 'description', 'image',)


class DoctorDetailForm(forms.ModelForm):
    class Meta:
        model = DoctorDetail
        fields = ('doctor_first_name', 'doctor_last_name', 'name_suffix', 'license_number', 'prescription_network_id', 'dea', 'doctor_phone_number', 'address_1','address_2', 'city','state','zip_code',)
        
class PharmacyDetailForm(forms.ModelForm):
    class Meta:
        model = PharmacyDetail
        fields = ('pharmacy_name','pharmacy_phone_number','address_1','address_2','city','state','zip_code',)
        
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        widgets = {
            'date_of_issuance': DateWidget(attrs={'id':"yourissuancedate"}, usel10n = True, bootstrap_version=3), 'refills': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No")))}
        fields = ('user', 'gender', 'date_of_issuance', 'days_supply', 'drug_name', 'drug_strength', 'dosage_form', 'frequency', 'quantity', 'npi_number', 'ndc_number', 'refills',)

class LabResultForm(forms.ModelForm):
    class Meta:
        model = LabResults
        widgets = {'test_date': DateWidget(attrs={'id':"testdate_id"}, usel10n = True, bootstrap_version=3)}
        fields = ('user','test_date','test_type', 'specific_gravity', 'pH','protein','glucose','ketones','blood','leukocyte_esterase','nitrite','bilirubin','urobilinogen',)

