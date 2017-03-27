from django.contrib import admin
from oneclickvitals.models import *
#from .models import UploadedImage

admin.site.register(Appointment)
admin.site.register(UserDetail)
admin.site.register(EmergencyContact)
admin.site.register(PatientMedicalHistory)
admin.site.register(FamilyMedicalHistory)
admin.site.register(VitalSigns)
admin.site.register(Diagnosis)
admin.site.register(LabTest)
admin.site.register(LabResults)
admin.site.register(Radiology)
admin.site.register(DoctorDetail)
admin.site.register(PharmacyDetail)
admin.site.register(Prescription)
#admin.site.register(UploadedImage, UploadedImageAdmin)


#class UploadedImageAdmin(admin.ModelAdmin):
#    pass

