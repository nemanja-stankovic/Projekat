import data
from appointment_time import *
from data import *
from saving_data import save_file_apointment_list,add_patient_to_file, save_examinations
from prescriptions import Prescription
from examination import Examination


def option_1_1():
    """Zakazivanje pregleda kod lekara opste prakse"""
    text_apointment = read_file("zakazani_pregledi.txt")
    word_list_apointment = split_words_by_slash(text_apointment)
    word_list_apointment_list = split_words_by_comma(word_list_apointment)
    indeks_polyclinic = int(input(f"Izaberite poikliniku\n{medical_center.show_polyclinics()}"))

    input_choise=int(input("Da li pacijent ima karton ?\n1)da\n2)ne\n"))
    if input_choise==1:
        pass
    else:
        if input_choise==2:
            patient_name=input("Unesite ime pacijenta:\n")
            patient_surname=input("Unesite prezime pacijenta:\n")
            patient_phone_number=input("Unesite broj telefona pacijenta:\n")
            patient_ID = medical_center.available_patient_ID()
            doctor_ID=input(f"Unesite ID izabranog lekara:\n{medical_center.show_doctors(indeks_polyclinic)}")
            adress=input("Unesite adresu pacijenta:\n")
            add_patient_to_file("pacijenti.txt",patient_name,patient_surname,patient_phone_number,patient_ID,doctor_ID,adress)
            new_patient=Patient(patient_name,patient_surname,patient_phone_number,patient_ID,doctor_ID,adress)
            medical_center.add_patient_to_list_of_patients(new_patient)
        else:
            print("Nevalidan unos")
    patient_number=input(f"Unesite broj kartona pacijenta\n{medical_center.show_patients()}")
    poliklinika = medical_center.list_of_polyclinics[indeks_polyclinic - 1]
    phone_number = poliklinika.phone_number
    doktor_ID=medical_center.find_doctor_ID_by_patient_ID(patient_number)
    check_if_patient_booked=is_patient_booked(word_list_apointment_list, phone_number, doktor_ID, patient_number)
    if check_if_patient_booked!=None:
        print(f"Pacijent vec ima zakazano na ovoj poliklinici kod ovog lekara, termin pregleda je:\n{check_if_patient_booked}")
    else:
        week_available_times_list_updated=remove_booked_apointments(week_available_times_list,word_list_apointment_list,phone_number,doktor_ID)
        day=int(input(f"Kog datuma zelite da zakazete pregled ?\n"
             f"{ days_string}"))
        time=int(input(f"{choice_times(week_available_times_list_updated,day)}"))
        apointment_time=week_available_times_list_updated[day-1][time-1]
        check_apointment=is_it_booked(word_list_apointment_list, phone_number, doktor_ID, apointment_time)
        apointment=Apointment(apointment_time,poliklinika.phone_number,doktor_ID,patient_number)
        word_list_apointment.append(apointment.__repr__())
        word_list_apointment_list = split_words_by_comma(word_list_apointment)
        save_file_apointment_list(word_list_apointment)
        print(f"Zakazan pregled dana {today}, pacijentu:{medical_center.find_patient_by_ID(patient_number)}\ntermin: {apointment_time}")

def option_1_2():
    """Pregled kod lekara opste prakse"""
    patient_number = input(f"Unesite broj kartona pacijenta\n{medical_center.show_patients()}")
    text_apointment = read_file("zakazani_pregledi.txt")
    word_list_apointment = split_words_by_slash(text_apointment)
    word_list_apointment_list = split_words_by_comma(word_list_apointment)
    if find_apointment_date(word_list_apointment_list,patient_number) != None:
        examination_date=find_apointment_date(word_list_apointment_list,patient_number)
        polyclinic_phone_number=find_polyclinic_number(word_list_apointment_list,patient_number)
        doctor_ID=find_doctor_ID(word_list_apointment_list,patient_number)
        doctor=medical_center.find_doctor_by_doctor_ID(doctor_ID)
        if doctor.specialty!="lekar_opste_prakse":
            print("Pacijent nema zakazano kod lekara opste prakse")
        else:
            poliklinika=medical_center.find_polyclinic_by_phone_number(polyclinic_phone_number)
            patient=medical_center.find_patient_by_ID(patient_number)
            diagnose = input("Unesite dijagnozu\n")
            index_medicine = int(input(f"Unesite lek za pacijenta\n{choice_prescription(word_list_medicines)}"))
            prescription=Prescription(word_list_medicines[index_medicine-1][0],
                                      word_list_medicines[index_medicine-1][1],
                                      word_list_medicines[index_medicine-1][2])
            examination=Examination(poliklinika,patient,doctor,diagnose,prescription,examination_date)
            medical_center.list_of_examinations.append(examination)
            print(examination)
            word_list_apointment=eliminate_apointment(word_list_apointment, examination_date, polyclinic_phone_number, doctor_ID, patient.patient_ID)
            save_file_apointment_list(word_list_apointment)
            save_examinations(medical_center.list_of_examinations)
    else:
        print("Pacijent sa tim brojem kartona nema zakazano")
def option_2_1():
    """Zakazivanje pregleda kod lekara specijaliste"""
    text_apointment = read_file("zakazani_pregledi.txt")
    word_list_apointment = split_words_by_slash(text_apointment)
    word_list_apointment_list = split_words_by_comma(word_list_apointment)
    indeks_polyclinic = int(input(f"Izaberite poikliniku\n{medical_center.show_polyclinics()}"))
    indeks_doctor = int(input((f"Izaberite lekara\n{medical_center.show_doctors_specialists(indeks_polyclinic - 1)}")))
    input_choise=int(input("Da li pacijent ima karton ?\n1)da\n2)ne\n"))
    if input_choise==1:
        pass
    else:
        if input_choise==2:
            patient_name=input("Unesite ime pacijenta:\n")
            patient_surname=input("Unesite prezime pacijenta:\n")
            patient_phone_number=input("Unesite broj telefona pacijenta:\n")
            patient_ID = medical_center.available_patient_ID()
            doctor_ID=input(f"Unesite ID izabranog lekara:\n{medical_center.show_doctors(indeks_polyclinic-1)}")
            adress=input("Unesite adresu pacijenta:\n")
            add_patient_to_file("pacijenti.txt",patient_name,patient_surname,patient_phone_number,patient_ID,doctor_ID,adress)
            new_patient=Patient(patient_name,patient_surname,patient_phone_number,patient_ID,doctor_ID,adress)
            medical_center.add_patient_to_list_of_patients(new_patient)
        else:
            print("Nevalidan unos")
    patient_number=input(f"Unesite broj kartona pacijenta\n{medical_center.show_patients()}")
    poliklinika = medical_center.list_of_polyclinics[indeks_polyclinic - 1]
    phone_number = poliklinika.phone_number
    lista_specijalista=medical_center.list_doctors_specialists()
    doktor=lista_specijalista[indeks_doctor-1]
    doktor_ID=doktor.ID_number
    check_if_patient_booked=is_patient_booked(word_list_apointment_list, phone_number, doktor_ID, patient_number)
    if check_if_patient_booked!=None:
        print(f"Pacijent vec ima zakazano na ovoj poliklinici kod ovog lekara, termin pregleda je:\n{check_if_patient_booked}")
    else:
        week_available_times_list_updated=remove_booked_apointments(week_available_times_list,word_list_apointment_list,phone_number,doktor_ID)
        day=int(input(f"Kog datuma zelite da zakazete pregled ?\n"
             f"{ days_string}"))
        time=int(input(f"{choice_times(week_available_times_list_updated,day)}"))
        apointment_time=week_available_times_list_updated[day-1][time-1]
        check_apointment=is_it_booked(word_list_apointment_list, phone_number, doktor_ID, apointment_time)
        apointment=Apointment(apointment_time,poliklinika.phone_number,doktor_ID,patient_number)
        word_list_apointment.append(apointment.__repr__())
        word_list_apointment_list = split_words_by_comma(word_list_apointment)
        save_file_apointment_list(word_list_apointment)
        print(f"Zakazan pregled dana {today}, pacijentu:{medical_center.find_patient_by_ID(patient_number)} kod doktora {doktor.name} {doktor.surname}\ntermin: {apointment_time}")

def option_2_2():
    """Pregled kod lekara specijaliste"""
    text_apointment = read_file("zakazani_pregledi.txt")
    word_list_apointment = split_words_by_slash(text_apointment)
    word_list_apointment_list = split_words_by_comma(word_list_apointment)
    indeks_polyclinic = int(input(f"Izaberite poikliniku\n{medical_center.show_polyclinics()}"))
    patient_number = input(f"Unesite broj kartona pacijenta\n{medical_center.show_patients()}")
    indeks_doctor = int(input((f"Izaberite lekara\n{medical_center.show_doctors_specialists(indeks_polyclinic - 1)}")))
    lista_specijalista=medical_center.list_doctors_specialists()
    doktor=lista_specijalista[indeks_doctor-1]
    doktor_ID=doktor.ID_number
    if find_apointment_date(word_list_apointment_list, patient_number) != None:
        examination_date = find_apointment_date(word_list_apointment_list, patient_number)
        polyclinic_phone_number = find_polyclinic_number(word_list_apointment_list, patient_number)
        if doktor.specialty== "lekar_opste_prakse":
            print("Pacijent nema zakazano kod lekara specijaliste")
        poliklinika = medical_center.find_polyclinic_by_phone_number(polyclinic_phone_number)
        patient = medical_center.find_patient_by_ID(patient_number)
        diagnose = input("Unesite dijagnozu\n")
        index_medicine = int(input(f"Unesite lek za pacijenta\n{choice_prescription(word_list_medicines)}"))
        prescription = Prescription(word_list_medicines[index_medicine - 1][0],
                                    word_list_medicines[index_medicine - 1][1],
                                    word_list_medicines[index_medicine - 1][2])
        examination = Examination(poliklinika, patient, doktor, diagnose, prescription, examination_date)
        medical_center.list_of_examinations.append(examination)
        print(examination)
        word_list_apointment = eliminate_apointment(word_list_apointment, examination_date,polyclinic_phone_number, doktor_ID, patient.patient_ID)
        save_file_apointment_list(word_list_apointment)
        save_examinations(medical_center.list_of_examinations)
    else:
        print("Pacijent sa tim brojem kartona nema zakazano")

def option_3_1():
    """dodatna opcija 1"""
    list_strings=[]
    for polyclinic in medical_center.polyclinics_with_most_number_of_specialists():
        for examination in medical_center.list_of_examinations:
            if examination.polyclinic.phone_number==polyclinic.phone_number:
                string=f"{examination.patient.name} {examination.patient.surname},{examination.examination_date}"
                list_strings.append(string)
    set_str=set(list_strings)
    print(set_str)
def option_3_2():
    """dodatna opcija 2"""
    list_of_doctors=medical_center.who_prescripted_more_than_ten()
    if list_of_doctors==[]:
        print("Nema lekara koji je prepisao vise od 10 recepata")
    else:
        print(list_of_doctors)
