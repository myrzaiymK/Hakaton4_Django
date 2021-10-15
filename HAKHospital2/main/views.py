from django.shortcuts import render
from .models import *

def hospital(request):
    return render(request, template_name='index.html')

def doctor(request):

    doctor = Doctor.objects.all()
    context = {
        'doctor': doctor,
    }
    return render(request, template_name='doctor.html', context=context)

def main(request):
    Maindocto = Maindoctor.objects.all()
    context = {
        'mdoctor': Maindocto,
    }
    return render(request, template_name='MainDR.html', context=context)
def nurse(request):
    nurse = Nurse.objects.all()
    context = {
        'nurse': nurse,
    }
    return render(request, template_name='nurse.html', context=context)
def patient(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient,
    }
    return render(request, template_name='patient.html', context=context)