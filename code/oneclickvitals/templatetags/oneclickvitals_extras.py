from django import template
from oneclickvitals.models import *

register = template.Library()

@register.inclusion_tag('oneclickvitals/appt.html')
def get_appointment_list():
    return {'appt': Appointment.objects.all().order_by('-appointment_date')}

@register.inclusion_tag('oneclickvitals/staff_appt.html')
def get_staff_appointment_list():
    return {'staff_appt': Appointment.objects.all().order_by('-appointment_date')}


@register.inclusion_tag('oneclickvitals/pats.html')
def get_patient_list():
    return {'pats': UserDetail.objects.all()}

@register.inclusion_tag('oneclickvitals/staff_pats.html')
def get_staff_patient_list():
    return {'staff_pats': UserDetail.objects.all()}


@register.inclusion_tag('oneclickvitals/rad_img.html')
def get_radiology_list():
    return {'rad_img': Radiology.objects.all().order_by('-created_date')}

@register.inclusion_tag('oneclickvitals/staff_rad_img.html')
def get_staff_radiology_list():
    return {'staff_rad_img': Radiology.objects.all().order_by('-created_date')}



@register.inclusion_tag('oneclickvitals/pres.html')
def get_prescription_list():
    return {'pres': Prescription.objects.all().order_by('-date_of_issuance')}

@register.inclusion_tag('oneclickvitals/staff_pres.html')
def get_staff_prescription_list():
    return {'staff_pres': Prescription.objects.all().order_by('-date_of_issuance')}


@register.inclusion_tag('oneclickvitals/diag.html')
def get_visit_records():
    return {'diag': Diagnosis.objects.all().order_by('-diagnosis_date')}

@register.inclusion_tag('oneclickvitals/staff_diag.html')
def get_staff_visit_records():
    return {'staff_diag': Diagnosis.objects.all().order_by('-diagnosis_date')}



@register.inclusion_tag('oneclickvitals/test.html')
def get_test_order_list():
    return {'test': LabTest.objects.all().order_by('-test_date')}

@register.inclusion_tag('oneclickvitals/staff_test.html')
def get_staff_test_order_list():
    return {'staff_test': LabTest.objects.all().order_by('-test_date')}



@register.inclusion_tag('oneclickvitals/result.html')
def get_lab_result_list():
    return {'result': LabResults.objects.all().order_by('-test_date')}

@register.inclusion_tag('oneclickvitals/staff_result.html')
def get_staff_lab_result_list():
    return {'staff_result': LabResults.objects.all().order_by('-test_date')}




@register.inclusion_tag('oneclickvitals/vital.html')
def get_vitalsigns_list():
    return {'vital': VitalSigns.objects.all().order_by('-visit_date')}

@register.inclusion_tag('oneclickvitals/staff_vital.html')
def get_staff_vitalsigns_list():
    return {'staff_vital': VitalSigns.objects.all().order_by('-visit_date')}