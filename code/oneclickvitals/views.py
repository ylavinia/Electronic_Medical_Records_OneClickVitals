from django.shortcuts import render, get_object_or_404, redirect, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from oneclickvitals.models import * 
#Appointment, PageAdmin, UserDetail, EmergencyContact, PatientMedicalHistory, Radiology, DoctorDetail, PharmacyDetail, Prescription
from oneclickvitals.forms import * 
#UserForm, UserDetailForm, NewPatientForm, AppointmentForm, EmergencyContactForm, PatientMedicalHistoryForm, PatientRadiologyImageForm, DoctorDetailForm, PharmacyDetailForm, PrescriptionForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.context_processors import csrf
from django.contrib import auth
from medical_project.settings import MEDIA_URL, MEDIA_ROOT
from django.utils import timezone
from django.template import RequestContext
from django.contrib import messages




def is_patient(user):
    return user.groups.filter(name="patient").exists()

def is_doctor(user):
    return user.groups.filter(name="doctor").exists()

def is_staff(user):
    return user.groups.filter(name="staff").exists()


def index(request):
    return render(request, 'index.html')

def index_patient(request):
    me = request.user
    pharmacy = PharmacyDetail.objects.get(user=me)
    return render(request, 'index_patient.html', {'pharmacy': pharmacy})

def index_staff(request):
    return render(request, 'index_staff.html')

def index_doctor(request):
    return render(request, 'index_doctor.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_active:

            if user.groups.filter(name="patient").exists():
                # Correct password, and the user is marked "active"
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/patient/")
            elif user.groups.filter(name="staff").exists():
                # Correct password, and the user is marked "active"
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/staff/")
            else:
                # Correct password, and the user is marked "active"
                login(request, user)
                return HttpResponseRedirect("/oneclickvitals/")
        else:
            return render(request, "registration/invalid_login.html")
    else:
        return render(request, 'registration/login.html')



def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request, 'registration/logout.html')

def invalid_login_view(request):
    if not user.is_authenticated():
         return render(request, 'registration/invalid_login.html')


def about(request):
    return render(request, 'oneclickvitals/about.html')

def staff_about(request):
    return render(request, 'oneclickvitals/staff_about.html')

def add_newpatient(request):
    print("in add_new")
    if request.method == 'POST':
        formA = NewPatientForm(request.POST)
        formB = UserDetailForm(request.POST)
        formC = EmergencyContactForm(request.POST)
        formD = PatientMedicalHistoryForm(request.POST)
        formE = FamilyMedicalHistoryForm(request.POST)

        formF = PharmacyDetailForm(request.POST)
        
        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid() and formF.is_valid():
            # Save the new category to the database.
            patientUser = formA.save(commit=False)
            patientUser.save()
            patientInfo = formB.save(commit=False)
            patientInfo.user = patientUser
            patientInfo.save()

            emergencyContact = formC.save(commit = False)
            emergencyContact.user = patientUser
            emergencyContact.save()
            patientMedicalHistory = formD.save(commit = False)
            patientMedicalHistory.user = patientUser
            patientMedicalHistory.save()
            familyMedicalHistory = formE.save(commit = False)
            familyMedicalHistory.user = patientUser
            familyMedicalHistory.save()
            pharmacy = formF.save(commit = False)
            pharmacy.user = patientUser
            pharmacy.save()
            patientUser.groups.add(Group.objects.get(name='patient'))
            print("saved new patient")

            # The user will be shown the patient profile page view.
            return patient_details(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        formA = NewPatientForm()
        formB = UserDetailForm()
        formC = EmergencyContactForm()
        formD = PatientMedicalHistoryForm()
        formE = FamilyMedicalHistoryForm()

        formF = PharmacyDetailForm()
        
    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/add_newpatient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE, 'formF': formF})


def staff_add_newpatient(request):
    print("in add_new")
    if request.method == 'POST':
        formA = NewPatientForm(request.POST)
        formB = UserDetailForm(request.POST)
        formC = EmergencyContactForm(request.POST)
        formD = PatientMedicalHistoryForm(request.POST)
        formE = FamilyMedicalHistoryForm(request.POST)

        formF = PharmacyDetailForm(request.POST)

        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid() and formF.is_valid():
            # Save the new category to the database.
            patientUser = formA.save(commit=False)
            patientUser.save()
            patientInfo = formB.save(commit=False)
            patientInfo.user = patientUser
            patientInfo.save()

            emergencyContact = formC.save(commit = False)
            emergencyContact.user = patientUser
            emergencyContact.save()
            patientMedicalHistory = formD.save(commit = False)
            patientMedicalHistory.user = patientUser
            patientMedicalHistory.save()
            familyMedicalHistory = formE.save(commit = False)
            familyMedicalHistory.user = patientUser
            familyMedicalHistory.save()
            pharmacy = formF.save(commit = False)
            pharmacy.user = patientUser
            pharmacy.save()
            patientUser.groups.add(Group.objects.get(name='patient'))
            print("saved new patient")

            # The user will be shown the patient profile page view.
            return staff_patient_details(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            #print(formA.errors)
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        formA = NewPatientForm()
        formB = UserDetailForm()
        formC = EmergencyContactForm()
        formD = PatientMedicalHistoryForm()
        formE = FamilyMedicalHistoryForm()

        formF = PharmacyDetailForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/staff_add_newpatient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE, 'formF': formF})




def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            appointment = form.save(commit=False)
            appointment.save()

            # The user will be shown the appointment detail page view.
            return appointment_details(request)
        else:
            #print (form.errors)
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        form = AppointmentForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/appointment.html', {'form': form})

def appointment_edit(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appt)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('appointment_details')
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        form = AppointmentForm(instance=appt)
    return render(request, 'oneclickvitals/appointment_edit.html', {'form': form})



def staff_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            appointment = form.save(commit=False)
            appointment.save()

            # The user will be shown the appointment detail page view.
            return staff_appointment_details(request)
        else:
            #print (form.errors)
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        form = AppointmentForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/staff_appointment.html', {'form': form})

def staff_appointment_edit(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appt)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('staff_appointment_details')
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        form = AppointmentForm(instance=appt)
    return render(request, 'oneclickvitals/staff_appointment_edit.html', {'form': form})





@login_required
def patient_details(request):
    details_list = UserDetail.objects.all()

    return render(request, 'oneclickvitals/patient_details.html', {'details': details_list})

@login_required
def staff_patient_details(request):
    details_list = UserDetail.objects.all()

    return render(request, 'oneclickvitals/staff_patient_details.html', {'details': details_list})

@login_required
def appointment_details(request):
    #appointment_list = Appointment.objects.all()
    appointment_list = Appointment.objects.all().order_by('-appointment_date')
    return render(request, 'oneclickvitals/appointment_details.html', {'appointment': appointment_list})

@login_required
def staff_appointment_details(request):
    #appointment_list = Appointment.objects.all()
    appointment_list = Appointment.objects.all().order_by('-appointment_date')
    return render(request, 'oneclickvitals/staff_appointment_details.html', {'appointment': appointment_list})


@login_required
def patient_profile(request, pk):
    me = User.objects.get(id=pk)
    profile = UserDetail.objects.get(user=me)
    
    emergency_contact= EmergencyContact.objects.get(user=me)
    medical_history = PatientMedicalHistory.objects.get(user=me)
    family_history = FamilyMedicalHistory.objects.get(user=me)
    pharmacy = PharmacyDetail.objects.get(user=me)
    if (VitalSigns.objects.filter(user=me).exists() or Diagnosis.objects.filter(patient=me).exists()):  
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date') 
        diagnosis_info = Diagnosis.objects.filter(patient=me).latest('diagnosis_date')
    
        context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history, 'family_history': family_history,'pharmacy': pharmacy,'vitalsigns_info': vitalsigns_info,'diagnosis_info': diagnosis_info}
    else:
        context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history, 'family_history': family_history,'pharmacy': pharmacy}
    
    return render(request, 'oneclickvitals/patient_profile.html', context_dict)


@login_required
def staff_patient_profile(request, pk):
    me = User.objects.get(id=pk)
    profile = UserDetail.objects.get(user=me)
    
    emergency_contact= EmergencyContact.objects.get(user=me)
    medical_history = PatientMedicalHistory.objects.get(user=me)
    family_history = FamilyMedicalHistory.objects.get(user=me)
    pharmacy = PharmacyDetail.objects.get(user=me)
    if (VitalSigns.objects.filter(user=me).exists() or Diagnosis.objects.filter(patient=me).exists()):  
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date') 
        diagnosis_info = Diagnosis.objects.filter(patient=me).latest('diagnosis_date')
    
        context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history, 'family_history': family_history,'pharmacy': pharmacy,'vitalsigns_info': vitalsigns_info,'diagnosis_info': diagnosis_info}
    else:
        context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history, 'family_history': family_history,'pharmacy': pharmacy}
    
    return render(request, 'oneclickvitals/staff_patient_profile.html', context_dict)

@login_required

def personal_appointment(request):
    me = request.user
    appointment_list = Appointment.objects.all()
    pharmacy = PharmacyDetail.objects.get(user=me)
    return render(request, 'oneclickvitals/personal_appointment.html', {'appointment': appointment_list, 'pharmacy': pharmacy})




@login_required
def personal_profile(request):
    
    me = request.user
    
    profile = UserDetail.objects.get(user=me)
    
    emergency_contact= EmergencyContact.objects.get(user=me)
    medical_history = PatientMedicalHistory.objects.get(user=me)
    family_history = FamilyMedicalHistory.objects.get(user=me)
    pharmacy = PharmacyDetail.objects.get(user=me)
    vitalsigns_info = VitalSigns.objects.filter(user=me)
    diagnosis_info = Diagnosis.objects.filter(patient=me)
    context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history,'family_history': family_history, 'pharmacy': pharmacy, 'vitalsigns_info': vitalsigns_info, 'diagnosis_info':diagnosis_info }
    
    return render(request, 'oneclickvitals/personal_profile.html', context_dict)


def edit_patient(request, pk):
    userDetail_instance = get_object_or_404(UserDetail, pk=pk)
    me = userDetail_instance.user
    newPatient_instance = User.objects.get(username=me)
    emergencyContact_instance = EmergencyContact.objects.get(user=me)
    patientMedicalHistory_instance = PatientMedicalHistory.objects.get(user=me)
    familyMedicalHistory_instance = FamilyMedicalHistory.objects.get(user=me)
    pharmacy_instance = PharmacyDetail.objects.get(user=me)
    if request.method == 'POST':
        formA = NewPatientForm(request.POST, instance = newPatient_instance)
        formB = UserDetailForm(request.POST, instance = userDetail_instance)
        formC = EmergencyContactForm(request.POST, instance = emergencyContact_instance)
        formD = PatientMedicalHistoryForm(request.POST, instance = patientMedicalHistory_instance)
        formE = FamilyMedicalHistoryForm(request.POST, instance = familyMedicalHistory_instance)
        formF = PharmacyDetailForm(request.POST, instance = pharmacy_instance )

        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid() and formF.is_valid():
            # Save the new category to the database.
            patientUser = formA.save()
            patientInfo = formB.save(commit=False)
            patientInfo.user = patientUser
            patientInfo.save()
            emergencyContact = formC.save(commit = False)
            emergencyContact.user = patientUser
            emergencyContact.save()
            patientMedicalHistory = formD.save(commit = False)
            patientMedicalHistory.user = patientUser
            patientMedicalHistory.save()
            familyMedicalHistory = formE.save(commit = False)
            familyMedicalHistory.user = patientUser
            familyMedicalHistory.save()
            pharmacy = formF.save(commit = False)
            pharmacy.user = patientUser
            pharmacy.save()
            patientUser.groups.add(Group.objects.get(name='patient'))
            print("saved new patient")

            # The user will be shown the patient profile page view.
            return patient_details(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        formA = NewPatientForm(instance = newPatient_instance)
        formB = UserDetailForm(instance = userDetail_instance)
        formC = EmergencyContactForm(instance = emergencyContact_instance)
        formD = PatientMedicalHistoryForm(instance = patientMedicalHistory_instance)
        formE = FamilyMedicalHistoryForm(instance = familyMedicalHistory_instance)
        formF = PharmacyDetailForm(instance = pharmacy_instance)
        
    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/edit_patient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE, 'formF': formF})


def staff_edit_patient(request, pk):
    userDetail_instance = get_object_or_404(UserDetail, pk=pk)
    me = userDetail_instance.user
    newPatient_instance = User.objects.get(username=me)
    emergencyContact_instance = EmergencyContact.objects.get(user=me)
    patientMedicalHistory_instance = PatientMedicalHistory.objects.get(user=me)
    familyMedicalHistory_instance = FamilyMedicalHistory.objects.get(user=me)
    pharmacy_instance = PharmacyDetail.objects.get(user=me)
    if request.method == 'POST':
        formA = NewPatientForm(request.POST, instance = newPatient_instance)
        formB = UserDetailForm(request.POST, instance = userDetail_instance)
        formC = EmergencyContactForm(request.POST, instance = emergencyContact_instance)
        formD = PatientMedicalHistoryForm(request.POST, instance = patientMedicalHistory_instance)
        formE = FamilyMedicalHistoryForm(request.POST, instance = familyMedicalHistory_instance)
        formF = PharmacyDetailForm(request.POST, instance = pharmacy_instance )

        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid() and formF.is_valid():
            # Save the new category to the database.
            patientUser = formA.save()
            patientInfo = formB.save(commit=False)
            patientInfo.user = patientUser
            patientInfo.save()
            emergencyContact = formC.save(commit = False)
            emergencyContact.user = patientUser
            emergencyContact.save()
            patientMedicalHistory = formD.save(commit = False)
            patientMedicalHistory.user = patientUser
            patientMedicalHistory.save()
            familyMedicalHistory = formE.save(commit = False)
            familyMedicalHistory.user = patientUser
            familyMedicalHistory.save()
            pharmacy = formF.save(commit = False)
            pharmacy.user = patientUser
            pharmacy.save()
            patientUser.groups.add(Group.objects.get(name='patient'))
            print("saved new patient")

            # The user will be shown the patient profile page view.
            return staff_patient_details(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        formA = NewPatientForm(instance = newPatient_instance)
        formB = UserDetailForm(instance = userDetail_instance)
        formC = EmergencyContactForm(instance = emergencyContact_instance)
        formD = PatientMedicalHistoryForm(instance = patientMedicalHistory_instance)
        formE = FamilyMedicalHistoryForm(instance = familyMedicalHistory_instance)
        formF = PharmacyDetailForm(instance = pharmacy_instance)
        
    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/staff_edit_patient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE, 'formF': formF})


@login_required
def add_lab_test(request):
    if request.method == 'POST':
        formK = LabTestForm(request.POST)

        if formK.is_valid():
            # Save the new category to the database.
            lab_test = formK.save(commit=False)
            lab_test.save()

            # The user will be shown the appointment detail page view.
            return labtest_list(request)
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")

    else:
        # If the request was not a POST, display the form to enter details.
        formK = LabTestForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/add_lab_test.html', {'formK': formK})






@login_required
def labtest_list(request):
    labtest = LabTest.objects.all()
    return render(request, 'oneclickvitals/labtest_list.html', {'labtest': labtest})


@login_required
def staff_labtest_list(request):
    labtest = LabTest.objects.all()
    return render(request, 'oneclickvitals/staff_labtest_list.html', {'labtest': labtest})


@login_required
def personal_labtest(request):
    me = request.user
    labtest_list = LabTest.objects.filter(user=me)
    pharmacy = PharmacyDetail.objects.get(user=me)
    return render(request, 'oneclickvitals/personal_labtest.html', {'labtest_list': labtest_list,'pharmacy': pharmacy,})


@login_required
def personal_labresult(request):
    me = request.user
    labtest = LabTest.objects.all()
    labresult_list = LabResults.objects.filter(user=me)
    pharmacy = PharmacyDetail.objects.get(user=me)
    

    return render(request, 'oneclickvitals/personal_labresult.html', {'labresult_list': labresult_list, 'pharmacy': pharmacy, 'labtest': labtest})


def vitalsigns(request):
    if request.method == 'POST':
        form = VitalSignsForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            vitalsigns = form.save(commit=False)
            vitalsigns.save()

            # The user will be shown the appointment detail page view.
            
            print ("Do I have the user id: ", vitalsigns.pk)
            
            return vitalsigns_list(request)
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")

    else:
        # If the request was not a POST, display the form to enter details.
        form = VitalSignsForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/vitalsigns.html', {'form': form})


def staff_vitalsigns(request):
    if request.method == 'POST':
        form = VitalSignsForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            vitalsigns = form.save(commit=False)
            vitalsigns.save()

            # The user will be shown the appointment detail page view.
            
            print ("Do I have the user id: ", vitalsigns.pk)
            
            return staff_vitalsigns_list(request)
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")

    else:
        # If the request was not a POST, display the form to enter details.
        form = VitalSignsForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/staff_vitalsigns.html', {'form': form})

def staff_vitalsigns_details(request, pk):
   
    vitalsigns_info = get_object_or_404(VitalSigns, pk=pk)
    return render(request, 'oneclickvitals/staff_vitalsigns_details.html', {'vitalsigns_info': vitalsigns_info})

def vitalsigns_details(request, pk):
    vitalsigns_info = VitalSigns.objects.get(pk=pk)
    me = vitalsigns_info.user
    date = vitalsigns_info.visit_date
    if Diagnosis.objects.filter(patient=me, diagnosis_date=date).exists():
        diagnosis_info = Diagnosis.objects.filter(patient=me, diagnosis_date=date)
        return render(request, 'oneclickvitals/vitalsigns_details.html', {'vitalsigns_info': vitalsigns_info, 'diagnosis_info': diagnosis_info})
        print(diagnosis_info.patient)
        print(diagnosis_info.diagnosis_date)
    else:
        return render(request, 'oneclickvitals/vitalsigns_details.html', {'vitalsigns_info': vitalsigns_info})

def staff_vitalsigns_list(request):
    vitalsigns = VitalSigns.objects.all().order_by('-visit_date')
    return render(request, 'oneclickvitals/staff_vitalsigns_list.html', {'vitalsigns': vitalsigns})

def vitalsigns_list(request):
    vitalsigns = VitalSigns.objects.all().order_by('-visit_date')
    return render(request, 'oneclickvitals/vitalsigns_list.html', {'vitalsigns': vitalsigns})
    

def visit_records(request):
    diagnosis = Diagnosis.objects.all().order_by('-diagnosis_date')
    return render(request, 'oneclickvitals/visit_records.html', {'diagnosis':diagnosis})

def staff_visit_records(request):
    diagnosis = Diagnosis.objects.all().order_by('-diagnosis_date')
    return render(request, 'oneclickvitals/staff_visit_records.html', {'diagnosis':diagnosis})

def diagnosis(request, pk):
    vitalsigns_info = get_object_or_404(VitalSigns, pk=pk)
    #diagnosis should be connected to vital signs of the current visit
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            diagnosis = form.save(commit=False)
            diagnosis.save()

            # The user will be shown the appointment detail page view.
            
            print ("Do I have the user id: ", diagnosis.pk)
            return diagnosis_details(request, diagnosis.pk)
        else:
            
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        form = DiagnosisForm()

    # Render the form with error messages (if any)
    return render_to_response('oneclickvitals/diagnosis.html', {'vitalsigns_info': vitalsigns_info, 'form': form}, context_instance=RequestContext(request))


def diagnosis_details(request, pk):
    
    diagnosis_info = get_object_or_404(Diagnosis, pk=pk)
    return render(request, 'oneclickvitals/diagnosis_details.html', {'diagnosis_info': diagnosis_info})


def personal_diagnosis(request):
    me = request.user
    diagnosis_info = Diagnosis.objects.filter(patient=me).order_by('-diagnosis_date')
    pharmacy = PharmacyDetail.objects.get(user=me)
    return render(request, 'oneclickvitals/personal_diagnosis.html', {'diagnosis_info': diagnosis_info, 'pharmacy':pharmacy})



def patient_radiology_image(request):
    if request.method == 'POST':
        form = PatientRadiologyImageForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the new image to the database.
            radiology_image = form.save(commit=False)
            radiology_image.save()

            # The user will be shown the radiology list.
            
        
            return redirect('radiology_list')
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")

    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientRadiologyImageForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/add_radiology.html', {'form': form})


def staff_patient_radiology_image(request):
    if request.method == 'POST':
        form = PatientRadiologyImageForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the new image to the database.
            radiology_image = form.save(commit=False)
            radiology_image.save()

            # The user will be shown the radiology list.
            #messages.success(request, 'Radiology image added.')
        
            return redirect('staff_radiology_list')
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
            

    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientRadiologyImageForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/staff_add_radiology.html', {'form': form})


@login_required
def radiology_list(request):
    radiology_images = Radiology.objects.all().order_by('-created_date')
    return render(request, 'oneclickvitals/radiology_list.html', {'radiology_images': radiology_images})

@login_required
def staff_radiology_list(request):
    radiology_images = Radiology.objects.all().order_by('-created_date')
    return render(request, 'oneclickvitals/staff_radiology_list.html', {'radiology_images': radiology_images})


@login_required
def view_radiology(request, pk):
    img = get_object_or_404(Radiology, pk=pk)
    return render_to_response('oneclickvitals/view_radiology.html', {'img':img}, context_instance=RequestContext(request) )


@login_required
def staff_view_radiology(request, pk):
    img = get_object_or_404(Radiology, pk=pk)
    return render_to_response('oneclickvitals/staff_view_radiology.html', {'img':img}, context_instance=RequestContext(request) )


@login_required
def edit_radiology(request, pk):
    img = get_object_or_404(Radiology, pk=pk)
    if request.method == 'POST':
        form = PatientRadiologyImageForm(request.POST, instance=img)

        if form.is_valid():
            # Save the new image to the database.
            radiology_image = form.save(commit=False)
            radiology_image.save()

            # The user will be shown the image list.
            return redirect('view_radiology', pk=img.pk)
        else:
            
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientRadiologyImageForm(instance=img)

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/edit_radiology.html', {'form': form})

@login_required
def staff_edit_radiology(request, pk):
    img = get_object_or_404(Radiology, pk=pk)
    if request.method == 'POST':
        form = PatientRadiologyImageForm(request.POST, instance=img)

        if form.is_valid():
            # Save the new image to the database.
            radiology_image = form.save(commit=False)
            radiology_image.save()

            # The user will be shown the image list.
            return redirect('staff_view_radiology', pk=img.pk)
        else:
            
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientRadiologyImageForm(instance=img)

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/staff_edit_radiology.html', {'form': form})



@login_required
def add_prescription(request):
    
    if request.method == 'POST':

        
        form = PrescriptionForm(request.POST)
        
        
        if form.is_valid():
            prescriptionDetail = form.save(commit=False)
            prescriptionDetail.save()
            
            
            return redirect('prescription_list')

        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.

        form = PrescriptionForm()
        

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/add_prescription.html', {'form': form })



def prescription_list(request):
    prescription = Prescription.objects.all().order_by('-date_of_issuance')
    return render(request, 'oneclickvitals/prescription_list.html', {'prescription': prescription})


def staff_prescription_list(request):
    prescription = Prescription.objects.all().order_by('-date_of_issuance')
    return render(request, 'oneclickvitals/staff_prescription_list.html', {'prescription': prescription})
    

def prescription_details(request, pk):
    prescription = Prescription.objects.get(pk=pk)
    me = prescription.user
    profile = UserDetail.objects.get(user=me)
    pharmacy = PharmacyDetail.objects.filter(user=me)[0]
    print(pharmacy.pharmacy_name)
    doctor = DoctorDetail.objects.all()[0]
    context_dict = {'profile':profile, 'prescription': prescription, 'pharmacy':pharmacy, 'doctor': doctor}
    return render(request, 'oneclickvitals/prescription_details.html', context_dict)

def staff_prescription_details(request, pk):
    prescription = Prescription.objects.get(pk=pk)
    me = prescription.user
    profile = UserDetail.objects.get(user=me)
    pharmacy = PharmacyDetail.objects.filter(user=me)[0]
    print(pharmacy.pharmacy_name)
    doctor = DoctorDetail.objects.all()[0]
    context_dict = {'profile':profile, 'prescription': prescription, 'pharmacy':pharmacy, 'doctor': doctor}
    return render(request, 'oneclickvitals/staff_prescription_details.html', context_dict)

def personal_prescription(request):
    me = request.user
    prescription_info = Prescription.objects.filter(user=me)

    pharmacy = PharmacyDetail.objects.get(user=me)

    context_dict = {'prescription_info': prescription_info, 'pharmacy': pharmacy }
    return render(request, 'oneclickvitals/personal_prescription.html',context_dict)

def visit_summary(request, pk):
    me = User.objects.get(id=pk)
    appointment_list = Appointment.objects.filter(user=me).latest('appointment_date')
    if VitalSigns.objects.filter(user=me).exists() and  Diagnosis.objects.filter(patient=me).exists() and Prescription.objects.filter(user=me).exists():
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date')
        diagnosis_info = Diagnosis.objects.filter(patient=me).latest('diagnosis_date')
        prescription_info = Prescription.objects.filter(user=me).latest('date_of_issuance')
        context_dict = {'appointment_list': appointment_list,  'vitalsigns_info':vitalsigns_info, 'diagnosis_info':diagnosis_info, 'prescription_info': prescription_info}
    elif VitalSigns.objects.filter(user=me).exists() and  Diagnosis.objects.filter(patient=me).exists():
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date')
        diagnosis_info = Diagnosis.objects.filter(patient=me).latest('diagnosis_date')
        context_dict = {'appointment_list': appointment_list, 'vitalsigns_info':vitalsigns_info, 'diagnosis_info':diagnosis_info }
    elif VitalSigns.objects.filter(user=me).exists():
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date')
        context_dict = {'appointment_list': appointment_list, 'vitalsigns_info':vitalsigns_info}
    else:
        context_dict = {'appointment_list': appointment_list}
    return render(request, 'oneclickvitals/visit_summary.html', context_dict)


def staff_visit_summary(request, pk):
    me = User.objects.get(id=pk)
    appointment_list = Appointment.objects.filter(user=me).latest('appointment_date')
    if VitalSigns.objects.filter(user=me).exists() and  Diagnosis.objects.filter(patient=me).exists() and Prescription.objects.filter(user=me).exists():
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date')
        diagnosis_info = Diagnosis.objects.filter(patient=me).latest('diagnosis_date')
        prescription_info = Prescription.objects.filter(user=me).latest('date_of_issuance')
        context_dict = {'appointment_list': appointment_list,  'vitalsigns_info':vitalsigns_info, 'diagnosis_info':diagnosis_info, 'prescription_info': prescription_info}
    elif VitalSigns.objects.filter(user=me).exists() and  Diagnosis.objects.filter(patient=me).exists():
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date')
        diagnosis_info = Diagnosis.objects.filter(patient=me).latest('diagnosis_date')
        context_dict = {'appointment_list': appointment_list, 'vitalsigns_info':vitalsigns_info, 'diagnosis_info':diagnosis_info }
    elif VitalSigns.objects.filter(user=me).exists():
        vitalsigns_info = VitalSigns.objects.filter(user=me).latest('visit_date')
        context_dict = {'appointment_list': appointment_list, 'vitalsigns_info':vitalsigns_info}
    else:
        context_dict = {'appointment_list': appointment_list}
    
    return render(request, 'oneclickvitals/staff_visit_summary.html', context_dict)



def add_doctor_information(request):
    if request.method == 'POST':
        form = DoctorDetailForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            doctorDetail = form.save(commit=False)
            doctorDetail.save()

            # The user will be shown the appointment detail page view.
            return view_doctor_information(request)
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        form = DoctorDetailForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/add_doctor_information.html', {'form': form})
    
@login_required
def view_doctor_information(request):
    doctor_details = DoctorDetail.objects.all()[0]
    return render(request, 'oneclickvitals/view_doctor_information.html', {'doctor_details':doctor_details}) 

@login_required
def staff_view_doctor_information(request):
    doctor_details = DoctorDetail.objects.all()[0]
    return render(request, 'oneclickvitals/staff_view_doctor_information.html', {'doctor_details':doctor_details}) 


@login_required
def add_lab_result(request, pk):
    results_info = get_object_or_404(LabTest, pk=pk)

    print("Labtest, User: ", results_info.user.first_name)

    if request.method == 'POST':
        formL = LabResultForm(request.POST)

        if formL.is_valid():
            # Save the new category to the database.
            
            lab_result = formL.save(commit=False)

            lab_result.save()
            
            # The user will be shown the appointment detail page view.
            
            return result_list(request)
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")

    else:
        # If the request was not a POST, display the form to enter details.
        formL = LabResultForm()

    # Render the form with error messages (if any)

    print("Labtest before render, User: ", results_info.user.first_name)

    return render(request, 'oneclickvitals/add_lab_result.html', {'formL': formL, 'results_info':results_info}, context_instance=RequestContext(request))
    

@login_required
def staff_add_lab_result(request, pk):
    results_info = get_object_or_404(LabTest, pk=pk)

    print("Labtest, User: ", results_info.user.first_name)

    if request.method == 'POST':
        formL = LabResultForm(request.POST)

        if formL.is_valid():
            # Save the new category to the database.
            
            lab_result = formL.save(commit=False)

            lab_result.save()
            
            # The user will be shown the appointment detail page view.
            
            return staff_result_list(request)
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
            
    else:
        # If the request was not a POST, display the form to enter details.
        formL = LabResultForm()

    # Render the form with error messages (if any)

    print("Labtest before render, User: ", results_info.user.first_name)

    return render(request, 'oneclickvitals/staff_add_lab_result.html', {'formL': formL, 'results_info':results_info}, context_instance=RequestContext(request))    

@login_required
def result_list(request):
    results = LabResults.objects.all().order_by('-test_date')
    labtest = LabTest.objects.all().order_by('-test_date')
    print("results.testtype:", results[1].test_type)
    return render(request, 'oneclickvitals/result_list.html', {'results': results, 'labtest': labtest})


@login_required
def staff_result_list(request):
    results = LabResults.objects.all().order_by('-test_date')
    labtest = LabTest.objects.all().order_by('-test_date')
    print("results.testtype:", results[1].test_type)
    return render(request, 'oneclickvitals/staff_result_list.html', {'results': results, 'labtest': labtest})


@login_required
def result_details(request, pk):
    me = User.objects.get(id=pk)
    result_info = get_object_or_404(LabResults, pk=pk)
    return render(request, 'oneclickvitals/result_details.html', {'result_info': result_info})


@login_required
def staff_result_details(request, pk):
    me = User.objects.get(id=pk)
    result_info = get_object_or_404(LabResults, pk=pk)
    return render(request, 'oneclickvitals/staff_result_details.html', {'result_info': result_info})


@login_required
def chart(request):
    print("in zing")
    me = request.user
    pharmacy = PharmacyDetail.objects.get(user=me)
    vsigns= VitalSigns.objects.filter(user=me)
    values = []
    for n in vsigns:
        values.append(n.heart_rate)
    values.reverse()
    weightvalues = []
    for n in vsigns:
        weightvalues.append(n.current_weight)
    weightvalues.reverse()

    print(weightvalues)
    dates = []
    for d in vsigns:
        dates.append(d.visit_date)
    print(dates)
    context_dict = {'values':values,'weightvalues':weightvalues, 'dates':dates, 'pharmacy': pharmacy}
    return render(request, 'oneclickvitals/chart.html',context_dict)

