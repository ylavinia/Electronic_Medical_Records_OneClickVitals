from django.conf.urls import patterns, url
from oneclickvitals import views
from django.conf import settings
from django.conf.urls.static import static
from oneclickvitals.views import view_radiology
from medical_project.settings import MEDIA_ROOT


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^staff_about/$', views.staff_about, name='staff_about'),
        url(r'^add_newpatient/$', views.add_newpatient, name='add_newpatient'),
        url(r'^staff_add_newpatient/$', views.staff_add_newpatient, name='staff_add_newpatient'),

        url(r'^appointment/$', views.appointment, name='appointment'),
        url(r'^staff_appointment/$', views.staff_appointment, name='staff_appointment'),
        url(r'^patient_details/$', views.patient_details, name='patient_details'),
        url(r'^staff_patient_details/$', views.staff_patient_details, name='staff_patient_details'),
        url(r'^appointment_details/$', views.appointment_details, name='appointment_details'),
        url(r'^appointment_edit/(?P<pk>[0-9]+)/$', views.appointment_edit, name='appointment_edit'),
        url(r'^staff_appointment_details/$', views.staff_appointment_details, name='staff_appointment_details'),
        url(r'^staff_appointment_edit/(?P<pk>[0-9]+)/$', views.staff_appointment_edit, name='staff_appointment_edit'),
        

        url(r'^personal_appointment/$', views.personal_appointment, name='personal_appointment'),
        url(r'^add_radiology/$', views.patient_radiology_image, name='patient_radiology_image'),
        url(r'^staff_add_radiology/$', views.staff_patient_radiology_image, name='staff_patient_radiology_image'),
    
        url(r'^radiology_list/$', views.radiology_list, name='radiology_list'),
        url(r'^staff_radiology_list/$', views.staff_radiology_list, name='staff_radiology_list'),
        url(r'^view_radiology/(?P<pk>[0-9]+)/$', views.view_radiology, name='view_radiology'),
        url(r'^staff_view_radiology/(?P<pk>[0-9]+)/$', views.staff_view_radiology, name='staff_view_radiology'),               
        
        url(r'^view_radiology/(?P<pk>[0-9]+)/edit/$', views.edit_radiology, name='edit_radiology'),
        url(r'^staff_view_radiology/(?P<pk>[0-9]+)/staff_edit/$', views.staff_edit_radiology, name='staff_edit_radiology'),
                       
                       
        url(r'^add_prescription/$', views.add_prescription, name='add_prescription'),
        url(r'^prescription_list/$', views.prescription_list, name='prescription_list'),
        url(r'^staff_prescription_list/$', views.staff_prescription_list, name='staff_prescription_list'),
        url(r'^prescription_details/(?P<pk>[0-9]+)/$', views.prescription_details, name='prescription_details'),
        url(r'^staff_prescription_details/(?P<pk>[0-9]+)/$', views.staff_prescription_details, name='staff_prescription_details'),
        url(r'^personal_prescription/$', views.personal_prescription, name='personal_prescription'),
        
        url(r'^visit_summary/(?P<pk>[0-9]+)/$', views.visit_summary, name='visit_summary'),
        url(r'^staff_visit_summary/(?P<pk>[0-9]+)/$', views.staff_visit_summary, name='staff_visit_summary'),
        url(r'^vitalsigns/$', views.vitalsigns, name='vitalsigns'),
        url(r'^staff_vitalsigns/$', views.staff_vitalsigns, name='staff_vitalsigns'),
        url(r'^vitalsigns_list/$', views.vitalsigns_list, name='vitalsigns_list'),
        url(r'^staff_vitalsigns_list/$', views.staff_vitalsigns_list, name='staff_vitalsigns_list'),
        url(r'^vitalsigns_details/(?P<pk>[0-9]+)/$', views.vitalsigns_details, name='vitalsigns_details'),
        url(r'^staff_vitalsigns_details/(?P<pk>[0-9]+)/$', views.staff_vitalsigns_details, name='staff_vitalsigns_details'),
        url(r'^visit_records/$', views.visit_records, name='visit_records'),
        url(r'^staff_visit_records/$', views.staff_visit_records, name='staff_visit_records'),
        url(r'^diagnosis/(?P<pk>[0-9]+)/$', views.diagnosis, name='diagnosis'),
        url(r'^diagnosis_details/(?P<pk>[0-9]+)/$', views.diagnosis_details, name='diagnosis_details'),
        url(r'^patient_profile/(?P<pk>[0-9]+)/$', views.patient_profile,name='patient_profile'),
        url(r'^staff_patient_profile/(?P<pk>[0-9]+)/$', views.staff_patient_profile,name='staff_patient_profile'),
        url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.edit_patient, name='edit_patient'),
        url(r'^staff_profile/(?P<pk>[0-9]+)/staff_edit/$', views.staff_edit_patient, name='staff_edit_patient'),
        url(r'^personal_profile/$', views.personal_profile, name='personal_profile'),
        url(r'^personal_diagnosis/$', views.personal_diagnosis, name='personal_diagnosis'),
        url(r'^add_doctor_information/$', views.add_doctor_information, name='add_doctor_information'),
        url(r'^view_doctor_information/$', views.view_doctor_information, name='view_doctor_information'),
        url(r'^staff_view_doctor_information/$', views.staff_view_doctor_information, name='staff_view_doctor_information'),               
                       
        url(r'^add_lab_test/$', views.add_lab_test, name='add_lab_test'),
        
        url(r'^labtest_list/$', views.labtest_list, name='labtest_list'),
        url(r'^staff_labtest_list/$', views.staff_labtest_list, name='staff_labtest_list'),
        url(r'^add_lab_result/(?P<pk>[0-9]+)/$', views.add_lab_result, name='add_lab_result'),
        url(r'^staff_add_lab_result/(?P<pk>[0-9]+)/$', views.staff_add_lab_result, name='staff_add_lab_result'),
        url(r'^result_list/$', views.result_list, name='result_list'),
        url(r'^staff_result_list/$', views.staff_result_list, name='staff_result_list'),
        url(r'^result_details/(?P<pk>[0-9]+)/$', views.result_details, name='result_details'),
        url(r'^staff_result_details/(?P<pk>[0-9]+)/$', views.staff_result_details, name='staff_result_details'),
        url(r'^personal_labtest/$', views.personal_labtest, name='personal_labtest'),
        url(r'^personal_labresult/$', views.personal_labresult, name='personal_labresult'),
        url(r'^chart/$', views.chart, name='chart'),
                      )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
