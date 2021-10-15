from django.db import models

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_work = models.CharField(max_length=100)
    doctor_age = models.CharField(max_length=50,default=20)
    doctor_experience = models.CharField(max_length=100)
    doctor_number = models.CharField(max_length=100)
    doctor_pasient = models.CharField(max_length=200,default=20)
    doctor_zam = models.CharField(max_length=100)
class Maindoctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_work = models.CharField(max_length=100)
    doctor_age = models.CharField(max_length=50,default=20)
    doctor_experience = models.CharField(max_length=100)
    doctor_pincode = models.CharField(max_length=15 , default=123134)
    doctor_number = models.CharField(max_length=100)
class Nurse(models.Model):
    nurse_name = models.CharField(max_length=20)
    nurse_pincode = models.CharField(max_length=9)
    nurse_age = models.CharField(max_length=4)
    nurse_number = models.CharField(max_length=15)
class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_pincode = models.CharField(max_length=9)
    patient_age = models.CharField(max_length=5)
    patient_number = models.CharField(max_length=15)
