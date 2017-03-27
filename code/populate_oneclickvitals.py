import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_project.settings')

import django
django.setup()

from oneclickvitals.models import Newpatient, Appointment


def populate():
    
    add_newpatient(
        patient_first_name = "Dani",
        patient_last_name = "Tadmori",
        patient_phone_number = "1234567890",
        patient_date_of_birth = 1980/12/12,
        patient_address = "some street",
        city = "some city")

    add_newpatient(
        patient_first_name = "YUkhe",
        patient_last_name = "Lovely",
        patient_phone_number = "1234567891",
        patient_date_of_birth = 1980/12/11,
        patient_address = "some street",
        city = "some city")


    # Print out what we have added to the user.
    for n in Newpatient.objects.all():

        print (str(n))

def add_newpatient(patient_first_name, patient_last_name, patient_phone_number,patient_date_of_birth, patient_address, city ):
    n = Newpatient.objects.get_or_create(firstname = patient_first_name, lastname = patient_last_name, phone = patient_phone_number,dob = patient_date_of_birth, address = patient_address, city = city)[0]
    return n

# Start execution here!
if __name__ == '__main__':
    print ("Starting oneclickvitals population script")
    populate()
