from polyclinics import Polyclinic
from medical_center import MedicalCentar
from patients import Patient
from examination import Examination
from prescriptions import Prescription
from usufull_functions import *

"""citanje text fajlova"""
text_poliklinike=read_file("poliklinike.txt")
text_lekari=read_file("lekari.txt")
text_pacijenti=read_file("pacijenti.txt")
text_medicines=read_file("medicines.txt")
text_examinations=read_file("pregledi.txt")

"""pretvaranje podataka iz text fajlova u liste"""
word_list_poliklinike=split_words(text_poliklinike)
word_list_lekari=split_words(text_lekari)
word_list_medicines=split_words(text_medicines)
word_list_examinations=split_words(text_examinations)
medical_center=MedicalCentar()
word_list_pacijenti=split_words(text_pacijenti)


"""Dodavanje liste pacijenata u medical_center"""
list_of_patients=[]
for j in range(1,len(word_list_pacijenti)):
    list_of_patients.append(Patient(word_list_pacijenti[j][1],word_list_pacijenti[j][2],word_list_pacijenti[j][4],word_list_pacijenti[j][0],word_list_pacijenti[j][5],word_list_pacijenti[j][3]))
medical_center.add_list_of_patients(list_of_patients)

"""Dodavanje poliklinika i liste lekara u medical_center"""
lista_lekara=[]
for i in range(1,len(word_list_lekari)):
    lista_lekara.append(Doctor(word_list_lekari[i][0],word_list_lekari[i][1],word_list_lekari[i][2],word_list_lekari[i][3],word_list_lekari[i][4]))

for i in range(1,len(word_list_poliklinike)):
    str_doctors=word_list_poliklinike[i][3].split(",")
    list_doctors=[]
    for str in str_doctors:
        ID=str.split(":")[1]
        doctor=find_doctor(lista_lekara,ID)
        list_doctors.append(doctor)
    medical_center.add_polyclinic(Polyclinic(word_list_poliklinike[i][0],word_list_poliklinike[i][1],word_list_poliklinike[i][2],list_doctors))

"""Dodavanje podataka o pregledima u medical_center"""
for examination in word_list_examinations:
    patient_ID = examination[0]
    doctor_ID = examination[1]
    diagnose = examination[2]
    medicine_code = examination[3]
    examination_date = examination[4]
    polyclinic_phone= examination[5]
    polyclinic=medical_center.find_polyclinic_by_phone_number(polyclinic_phone)
    doctor=medical_center.find_doctor_by_doctor_ID(doctor_ID)
    patient=medical_center.find_patient_by_ID(patient_ID)
    prescription=find_medicine_by_code(word_list_medicines,medicine_code)
    medical_center.list_of_examinations.append(Examination(polyclinic,patient,doctor,diagnose,prescription,examination_date))

