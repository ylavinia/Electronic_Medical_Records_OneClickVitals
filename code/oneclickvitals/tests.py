from django.test import TestCase
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, RequestContext
from .models import *
from .forms import *
from django.http import HttpRequest
from medical_project.settings import *
from django.conf import settings
from django.utils.importlib import import_module

class UserDetailTest(TestCase):
    def create_user_object(self, username="me"):
        return User.objects.create(username=username)
    
    def create_user_detail_object(self, user="me", gender="female"):
        the_user = self.create_user_object(user)
        return UserDetail.objects.create(user=the_user, gender=gender)
    
    def test_user_detail_object_creation(self):
        the_user_detail = self.create_user_detail_object()
        self.assertTrue(isinstance(the_user_detail, UserDetail))
        self.assertEqual(the_user_detail.__str__(), "me")
        self.assertEqual(the_user_detail.gender, "female")
        
    def test_get_user_detail_object(self, pk=1):
        the_user_detail = self.create_user_detail_object()
        you = User.objects.get(pk=pk)
        user_detail_instance = UserDetail.objects.get(user=you)
        self.assertEqual(user_detail_instance.__str__(), "me")
        

class AppointmentTest(TestCase):
    def create_user_object(self, username="me"):
        return User.objects.create(username=username)
    
    def create_appointment_object(self, user="me", type_of_appointment="follow-up"):
        the_user = self.create_user_object(user)
        return Appointment.objects.create(user=the_user, type_of_appointment=type_of_appointment)
    
    def test_appointment_object_creation(self):
        the_appt = self.create_appointment_object()
        self.assertTrue(isinstance(the_appt, Appointment))
        self.assertEqual(the_appt.__str__(), "me")
        self.assertEqual(the_appt.type_of_appointment, "follow-up")
        
    def test_get_appointment_object(self, pk=1):
        the_appt = self.create_appointment_object()
        blah = User.objects.get(pk=pk)
        appointment_instance = Appointment.objects.get(user=blah)
        self.assertEqual(appointment_instance.type_of_appointment, "follow-up")
        
    def test_load_appointment_list(request):
        context = {'appointments': Appointment.objects.all().order_by('-appointment_date')}
        return render(request, 'oneclickvitals/appointment_details.html', context)
    
    
class PharmacyDetailTest(TestCase):
   
    def create_user_object(self, username="me"):
        return User.objects.create(username=username)
    
    def create_pharmacy_detail_object(self, user="me", pharmacy_name="CVS", address_1="Street"):
        the_user = self.create_user_object(user)
        return PharmacyDetail.objects.create(user=the_user, pharmacy_name=pharmacy_name, address_1=address_1)
        
    def test_pharmacy_detail_object_creation(self):
        the_pharmacy= self.create_pharmacy_detail_object()
        self.assertTrue(isinstance(the_pharmacy, PharmacyDetail))
        self.assertEqual(the_pharmacy.__str__(), "me")
        self.assertEqual(the_pharmacy.pharmacy_name, "CVS")
        self.assertEqual(the_pharmacy.address_1, "Street")
        
    def test_get_pharmacy_object(self, pk=1):
        the_pharmacy = self.create_pharmacy_detail_object()
        me = User.objects.get(pk=pk)
        pharmacy_instance = PharmacyDetail.objects.get(user=me)
        self.assertEqual(pharmacy_instance.__str__(), "me")
        

        
class VitalSignsTest(TestCase):
   
    def create_user_object(self, username="me"):
        return User.objects.create(username=username)
    
    def create_vitalsigns_object(self, user="me", heart_rate="100", blood_pressure="120/70"):
        the_user = self.create_user_object(user)
        return VitalSigns.objects.create(user=the_user, heart_rate=heart_rate, blood_pressure=blood_pressure)
        
    def test_vitalsigns_object_creation(self):
        the_vitalsigns= self.create_vitalsigns_object()
        self.assertTrue(isinstance(the_vitalsigns, VitalSigns))
        self.assertEqual(the_vitalsigns.user.username, "me")
        self.assertEqual(the_vitalsigns.heart_rate, "100")
        self.assertEqual(the_vitalsigns.blood_pressure, "120/70")
        
    def test_get_vitalsigns_object(self, pk=1):
        the_vitalsigns = self.create_vitalsigns_object()
        me = User.objects.get(pk=pk)
        vitalsigns_instance = VitalSigns.objects.get(user=me)
        self.assertEqual(vitalsigns_instance.user.username, "me")
        
    def test_load_vitalsigns_list(request):
            context = {'vitalsigns': VitalSigns.objects.all().order_by('-visit_date')}
            return render(request, 'oneclickvitals/vitalsigns_list.html', context)
        
    def test_load_vitalsigns_details(self, request=HttpRequest(), pk=1):
        the_vitalsigns = self.create_vitalsigns_object()
        the_request=request
        vitalsigns_instance = VitalSigns.objects.get(pk=pk)
        return render(the_request, 'oneclickvitals/vitalsigns_details.html', {'vitalsigns_instance': vitalsigns_instance})

        
        
class DiagnosisTest(TestCase):
   
    def create_user_object(self, username="me"):
        return User.objects.create(username=username)
    
    def create_diagnosis_object(self, patient="me", complaint="headache", diagnosis="vertigo"):
        the_patient = self.create_user_object(patient)
        return Diagnosis.objects.create(patient=the_patient, complaint=complaint, diagnosis=diagnosis)
        
    def test_diagnosis_object_creation(self):
        the_diagnosis= self.create_diagnosis_object()
        self.assertTrue(isinstance(the_diagnosis, Diagnosis))
        self.assertEqual(the_diagnosis.patient.username, "me")
        self.assertEqual(the_diagnosis.complaint, "headache")
        self.assertEqual(the_diagnosis.diagnosis, "vertigo")
        
    def test_get_diagnosis_object(self, pk=1):
        the_diagnosis = self.create_diagnosis_object()
        me = User.objects.get(pk=pk)
        diagnosis_instance = Diagnosis.objects.get(patient=me)
        self.assertEqual(diagnosis_instance.patient.username, "me")
        
    def test_load_diagnosis_list(request):
            context = {'diagnosis': Diagnosis.objects.all().order_by('-diagnosis_date')}
            return render(request, 'oneclickvitals/visit_records.html', context)
        
    def test_load_diagnosis_details(self, request=HttpRequest(), pk=1):
        the_diagnosis = self.create_diagnosis_object()
        me = User.objects.get(pk=pk)
        diagnosis_instance = Diagnosis.objects.get(patient=me)
        self.assertEqual(diagnosis_instance.patient.username, "me")

    def test_personal_diagnosis(self):
        
        the_diagnosis = self.create_diagnosis_object()
        request = HttpRequest()
        request.user = the_diagnosis.patient
        diagnosis_instance = Diagnosis.objects.filter(patient=request.user)
        return render(request, 'oneclickvitals/personal_diagnosis.html', {'diagnosis_instance': diagnosis_instance})
    
    
class PrescriptionTest(TestCase):

    def create_user_object(self, username="me"):
        return User.objects.create(username=username)

    def create_prescription_object(self, user="me", gender="female", days_supply="10", drug_name="aspirin",
                                   drug_strength="250mg", dosage_form="PO (by mouth)", frequency="daily",
                                   npi_number="1234567890", ndc_number="1234-5678-9"):
        the_user = self.create_user_object(user)
        return Prescription.objects.create(user=the_user, gender=gender, days_supply=days_supply,
                                           drug_name=drug_name, drug_strength=drug_strength, dosage_form=dosage_form,
                                           frequency=frequency, npi_number=npi_number, ndc_number=ndc_number)

    def test_prescription_object_creation(self):
        the_prescription= self.create_prescription_object()
        self.assertTrue(isinstance(the_prescription, Prescription))
        self.assertEqual(the_prescription.user.username, "me")
        self.assertEqual(the_prescription.gender, "female")
        self.assertEqual(the_prescription.days_supply, "10")
        self.assertEqual(the_prescription.drug_name, "aspirin")
        self.assertEqual(the_prescription.drug_strength, "250mg")
        self.assertEqual(the_prescription.dosage_form, "PO (by mouth)")
        self.assertEqual(the_prescription.frequency, "daily")
        self.assertEqual(the_prescription.npi_number, "1234567890")
        self.assertEqual(the_prescription.ndc_number, "1234-5678-9")


    def test_get_prescription_object(self, pk=1):
        the_prescription = self.create_prescription_object()
        me = User.objects.get(pk=pk)
        prescription_instance = Prescription.objects.get(user=me)
        self.assertEqual(prescription_instance.user.username, "me")
        self.assertEqual(the_prescription.gender, "female")
        self.assertEqual(the_prescription.days_supply, "10")
        self.assertEqual(the_prescription.drug_name, "aspirin")
        self.assertEqual(the_prescription.drug_strength, "250mg")
        self.assertEqual(the_prescription.dosage_form, "PO (by mouth)")
        self.assertEqual(the_prescription.frequency, "daily")
        self.assertEqual(the_prescription.npi_number, "1234567890")
        self.assertEqual(the_prescription.ndc_number, "1234-5678-9")


    def test_load_prescription_list(request):
            context = {'prescription': Prescription.objects.all().order_by('-date_of_issuance')}
            return render(request, 'oneclickvitals/prescription_list.html', context)

    def test_load_prescription_details(self, request=HttpRequest(), pk=1):
        the_prescription = self.create_prescription_object()
        me = User.objects.get(pk=pk)
        prescription_instance = Prescription.objects.get(user=me)
        self.assertEqual(prescription_instance.user.username, "me")

    def test_personal_prescription(self):
        the_prescription = self.create_prescription_object()
        request = HttpRequest()
        request.user = the_prescription.user
        prescription_instance = Prescription.objects.filter(user=request.user)
        return render(request, 'oneclickvitals/personal_prescription.html', {'prescription_instance': prescription_instance})


class LabResultsTest(TestCase):

    def create_user_object(self, username="me"):
        return User.objects.create(username=username)

    def create_labresults_object(self, user="me", test_type="urine culture", specific_gravity="1.002",
                                pH="7.5", protein="6", glucose="7", ketones="positive",
                                blood="negative", leukocyte_esterase="positive", nitrite="positive",
                                bilirubin="negative", urobilinogen="negative"):
        the_user = self.create_user_object(user)
        return LabResults.objects.create(user=the_user, test_type=test_type, specific_gravity=specific_gravity,
                                        pH=pH, protein=protein, glucose=glucose, ketones=ketones,
                                        blood=blood, leukocyte_esterase=leukocyte_esterase, nitrite=nitrite,
                                        bilirubin=bilirubin, urobilinogen=urobilinogen)

    def test_labresults_object_creation(self):
        the_labresults= self.create_labresults_object()
        self.assertTrue(isinstance(the_labresults, LabResults))
        self.assertEqual(the_labresults.user.username, "me")
        self.assertEqual(the_labresults.test_type, "urine culture")
        self.assertEqual(the_labresults.specific_gravity, "1.002")
        self.assertEqual(the_labresults.pH, "7.5")
        self.assertEqual(the_labresults.protein, "6")
        self.assertEqual(the_labresults.glucose, "7")
        self.assertEqual(the_labresults.ketones, "positive")
        self.assertEqual(the_labresults.blood, "negative")
        self.assertEqual(the_labresults.leukocyte_esterase, "positive")
        self.assertEqual(the_labresults.nitrite, "positive")
        self.assertEqual(the_labresults.bilirubin, "negative")
        self.assertEqual(the_labresults.urobilinogen, "negative")

    def test_get_labresults_object(self, pk=1):
        the_labresults = self.create_labresults_object()
        me = User.objects.get(pk=pk)
        labresults_instance = LabResults.objects.get(user=me)
        self.assertEqual(labresults_instance.user.username, "me")
        self.assertEqual(the_labresults.test_type, "urine culture")
        self.assertEqual(the_labresults.specific_gravity, "1.002")
        self.assertEqual(the_labresults.pH, "7.5")
        self.assertEqual(the_labresults.protein, "6")
        self.assertEqual(the_labresults.glucose, "7")
        self.assertEqual(the_labresults.ketones, "positive")
        self.assertEqual(the_labresults.blood, "negative")


    def test_load_labresults_list(request):
            context = {'labresults': LabResults.objects.all().order_by('-test_date')}
            return render(request, 'oneclickvitals/result_list.html', context)

    def test_load_labresults_details(self, request=HttpRequest(), pk=1):
        the_labresults = self.create_labresults_object()
        the_request=request
        labresults_instance = LabResults.objects.get(pk=pk)
        return render(the_request, 'oneclickvitals/result_details.html', {'labresults_instance': labresults_instance})


class LabTestTest(TestCase):

    def create_user_object(self, username="me"):
        return User.objects.create(username=username)

    def create_labtest_object(self, user="me", urine_culture="yes", blood_culture="no",
                                    allergy_test="no", blood_glucose="yes", thyroid="no", viral_test="no",
                                    pregnancy_test="no", x_ray="none"):
        the_user = self.create_user_object(user)
        return LabTest.objects.create(user=the_user, urine_culture=urine_culture, blood_culture=blood_culture,
                                      allergy_test=allergy_test, blood_glucose=blood_glucose, thyroid=thyroid,
                                      viral_test=viral_test, pregnancy_test=pregnancy_test, x_ray=x_ray)

    def test_labtest_object_creation(self):
        the_labtest= self.create_labtest_object()
        self.assertTrue(isinstance(the_labtest, LabTest))
        self.assertEqual(the_labtest.__str__(), "me")
        self.assertEqual(the_labtest.urine_culture, "yes")
        self.assertEqual(the_labtest.blood_culture, "no")
        self.assertEqual(the_labtest.allergy_test, "no")
        self.assertEqual(the_labtest.blood_glucose, "yes")
        self.assertEqual(the_labtest.thyroid, "no")
        self.assertEqual(the_labtest.viral_test, "no")
        self.assertEqual(the_labtest.pregnancy_test, "no")
        self.assertEqual(the_labtest.x_ray, "none")

    def test_get_labtest_object(self, pk=1):
        the_labtest = self.create_labtest_object()
        me = User.objects.get(pk=pk)
        labtest_instance = LabTest.objects.get(user=me)
        self.assertEqual(labtest_instance.__str__(), "me")
        self.assertEqual(the_labtest.urine_culture, "yes")
        self.assertEqual(the_labtest.blood_culture, "no")
        self.assertEqual(the_labtest.allergy_test, "no")
        self.assertEqual(the_labtest.blood_glucose, "yes")
        self.assertEqual(the_labtest.thyroid, "no")
        self.assertEqual(the_labtest.viral_test, "no")
        self.assertEqual(the_labtest.pregnancy_test, "no")
        self.assertEqual(the_labtest.x_ray, "none")


    def test_personal_labtest(self):
        the_labtest = self.create_labtest_object()
        request = HttpRequest()
        request.user = the_labtest.user
        labtest_instance = LabTest.objects.filter(user=request.user)
        return render(request, 'oneclickvitals/personal_labtest.html', {'labtest_instance': labtest_instance})


class EmergencyContactTest(TestCase):

    def create_user_object(self, username="me"):
        return User.objects.create(username=username)

    def create_emergency_contact_object(self, user="me", contact_first_name="first", contact_last_name="last",
                                    relationship="spouse", contact_phone_number="(714) 245-0987"):
        the_user = self.create_user_object(user)
        return EmergencyContact.objects.create(user=the_user, contact_first_name=contact_first_name, contact_last_name=contact_last_name,
                                      relationship=relationship, contact_phone_number=contact_phone_number)

    def test_emergency_contact_object_creation(self):
        the_emergency_contact= self.create_emergency_contact_object()
        self.assertTrue(isinstance(the_emergency_contact, EmergencyContact))
        self.assertEqual(the_emergency_contact.__str__(), "me")
        self.assertEqual(the_emergency_contact.contact_first_name, "first")
        self.assertEqual(the_emergency_contact.contact_last_name, "last")
        self.assertEqual(the_emergency_contact.relationship, "spouse")
        self.assertEqual(the_emergency_contact.contact_phone_number, "(714) 245-0987")

    def test_get_emergency_contact_object(self, pk=1):
        the_emergency_contact = self.create_emergency_contact_object()
        me = User.objects.get(pk=pk)
        emergency_contact_instance = EmergencyContact.objects.get(user=me)
        self.assertEqual(emergency_contact_instance.__str__(), "me")
        self.assertEqual(the_emergency_contact.contact_first_name, "first")
        self.assertEqual(the_emergency_contact.contact_last_name, "last")
        self.assertEqual(the_emergency_contact.relationship, "spouse")
        self.assertEqual(the_emergency_contact.contact_phone_number, "(714) 245-0987")


    def test_personal_emergency_contact(self):
        the_emergency_contact = self.create_emergency_contact_object()
        request = HttpRequest()
        request.user = the_emergency_contact.user
        emergency_contact_instance = EmergencyContact.objects.filter(user=request.user)
        return render(request, 'oneclickvitals/personal_profile.html', {'emergency_contact_instance': emergency_contact_instance})


class PatientMedicalHistoryTest(TestCase):

    def create_user_object(self, username="me"):
        return User.objects.create(username=username)

    def create_patient_medical_history_object(self, user="me", height="68", weight="170",
                                    blood_type="o+", allergies="None", current_medications="None",
                                    chief_complaint="Pain", surgical_history="None",
                                    medical_history="None", social_habits="Smoking"):
        the_user = self.create_user_object(user)
        return PatientMedicalHistory.objects.create(user=the_user, height=height, weight=weight,
                                      blood_type=blood_type, allergies=allergies, current_medications=current_medications,
                                      chief_complaint=chief_complaint, surgical_history=surgical_history,
                                      medical_history=medical_history, social_habits=social_habits)

    def test_patient_medical_history_object_creation(self):
        the_patient_medical_history= self.create_patient_medical_history_object()
        self.assertTrue(isinstance(the_patient_medical_history, PatientMedicalHistory))
        self.assertEqual(the_patient_medical_history.__str__(), "me")
        self.assertEqual(the_patient_medical_history.height, "68")
        self.assertEqual(the_patient_medical_history.weight, "170")
        self.assertEqual(the_patient_medical_history.blood_type, "o+")
        self.assertEqual(the_patient_medical_history.allergies, "None")
        self.assertEqual(the_patient_medical_history.current_medications, "None")
        self.assertEqual(the_patient_medical_history.chief_complaint, "Pain")
        self.assertEqual(the_patient_medical_history.surgical_history, "None")
        self.assertEqual(the_patient_medical_history.medical_history, "None")
        self.assertEqual(the_patient_medical_history.social_habits, "Smoking")

    def test_get_patient_medical_history_object(self, pk=1):
        the_patient_medical_history = self.create_patient_medical_history_object()
        me = User.objects.get(pk=pk)
        patient_medical_history_instance = PatientMedicalHistory.objects.get(user=me)
        self.assertEqual(patient_medical_history_instance.__str__(), "me")
        self.assertEqual(the_patient_medical_history.height, "68")
        self.assertEqual(the_patient_medical_history.weight, "170")
        self.assertEqual(the_patient_medical_history.blood_type, "o+")
        self.assertEqual(the_patient_medical_history.allergies, "None")
        self.assertEqual(the_patient_medical_history.current_medications, "None")
        self.assertEqual(the_patient_medical_history.chief_complaint, "Pain")
        self.assertEqual(the_patient_medical_history.surgical_history, "None")
        self.assertEqual(the_patient_medical_history.medical_history, "None")
        self.assertEqual(the_patient_medical_history.social_habits, "Smoking")


    def test_personal_medical_history(self):
        the_personal_medical_history = self.create_patient_medical_history_object()
        request = HttpRequest()
        request.user = the_personal_medical_history.user
        personal_medical_history_instance = PatientMedicalHistory.objects.filter(user=request.user)
        return render(request, 'oneclickvitals/personal_profile.html', {'personal_medical_history_instance': personal_medical_history_instance})



