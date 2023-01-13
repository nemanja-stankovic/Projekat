from polyclinics import Polyclinic
import typing as t
from patients import Patient
from examination import Examination


class MedicalCentar:

    def __init__(self,list_of_patients:t.List[Patient]=[],list_of_polyclinics: t.List[Polyclinic]=[],list_of_examinations:t.List[Examination]=[]):
        self.list_of_polyclinics=list_of_polyclinics
        self.list_of_patients=list_of_patients
        self.list_of_examinations=list_of_examinations

    def add_polyclinic(self,polyclinic:Polyclinic):
        self.list_of_polyclinics.append(polyclinic)

    def __repr__(self):
        return f"{self.list_of_polyclinics}"

    def show_polyclinics(self):
        polyclinics_string=""
        i=0
        for polyclinic in self.list_of_polyclinics:
            i+=1
            line=f"{i}) {polyclinic.name}, {polyclinic.place}, br. telefona {polyclinic.phone_number}\n"
            polyclinics_string+=line
        return polyclinics_string

    def show_doctors(self,index):
        doctors_string=""
        i=0
        polyclinic=self.list_of_polyclinics[index]
        for doctor in polyclinic.list_of_doctors:
            if doctor.specialty=="lekar_opste_prakse":
                i+=1
                line=f"{i}) {doctor.ID_number} {doctor.name}, {doctor.surname},  {doctor.specialty}\n"
                doctors_string+=line
        return doctors_string

    def show_doctors_specialists(self,index_polyclinic):
        doctors_string=""
        i=0
        polyclinic=self.list_of_polyclinics[index_polyclinic]
        for doctor in polyclinic.list_of_doctors:
            if doctor.specialty!="lekar_opste_prakse":
                i+=1
                line=f"{i}) {doctor.ID_number} {doctor.name}, {doctor.surname},  {doctor.specialty}\n"
                doctors_string+=line
        return doctors_string

    def add_list_of_patients(self,list_of_patients:t.List[Patient]):
        self.list_of_patients=list_of_patients

    def show_patients(self) -> str:
        patients=""
        for i in range(len(self.list_of_patients)):
            line=str(self.list_of_patients[i])
            patients+=line+"\n"
        return patients

    def add_patient_to_list_of_patients(self,patient:Patient):
        self.list_of_patients.append(patient)

    def find_doctor_ID_by_patient_ID(self,patient_ID: str)->str:
        for patient in self.list_of_patients:
            if patient.patient_ID==patient_ID:
                return patient.doctor_ID

    def find_patient_by_ID(self,patient_ID: str)-> Patient:
        for patient in self.list_of_patients:
            if patient.patient_ID==patient_ID:
                return patient

    def find_doctor_by_doctor_ID(self,doctor_ID):
        for polyclinic in self.list_of_polyclinics:
            for doctor in polyclinic.list_of_doctors:
                if doctor.ID_number==doctor_ID:
                    return doctor

    def find_polyclinic_by_phone_number(self,phone_number: str)-> Polyclinic:
        for polyclinic in self.list_of_polyclinics:
            if polyclinic.phone_number==phone_number:
                return polyclinic

    def list_doctors_specialists(self)-> list:
        list_of_specialists=[]
        for polyclinic in self.list_of_polyclinics:
            for doctor in polyclinic.list_of_doctors:
                if doctor.specialty!="lekar_opste_prakse":
                    list_of_specialists.append(doctor)
        return list_of_specialists

    def number_of_patiens(self):
        number_of_patients=len(self.list_of_patients)
        return number_of_patients

    def last_number_patient(self):
        last_number=int(self.list_of_patients[len(self.list_of_patients)-1].patient_ID)
        return last_number

    def available_patient_ID(self):
        available_ID=self.last_number_patient()+1
        available_ID_str=str(available_ID)
        return available_ID_str

    def polyclinic_number_of_specialist(self,polyclinic):
        count=0
        for doctor in polyclinic.list_of_doctors:
            if doctor.specialty != "lekar_opste_prakse":
                count+=1
        return count

    def polyclinics_with_most_number_of_specialists(self):
        highest=0
        list_highest=[]
        for polyclinic in self.list_of_polyclinics:
            if self.polyclinic_number_of_specialist(polyclinic)>highest:
                highest=self.polyclinic_number_of_specialist(polyclinic)
                polyclinic_highest=polyclinic
        list_highest.append(polyclinic_highest)
        for polyclinic in self.list_of_polyclinics:
            if self.polyclinic_number_of_specialist(polyclinic) == highest:
                list_highest.append(polyclinic)
        return list_highest

    def how_many_prescriptions_for_doctor(self,doctor_ID):
        number=0
        for examination in self.list_of_examinations:
            if examination.doctor.ID_number==doctor_ID:
                number+=1
        return number

    def who_prescripted_more_than_ten(self):
        list_of_doctors_who_pres_more_than_ten=[]
        for polyclinic in self.list_of_polyclinics:
            for doctor in polyclinic.list_of_doctors:
                if self.how_many_prescriptions_for_doctor(doctor.ID_number)>10:
                    list_of_doctors_who_pres_more_than_ten.append(doctor)
        return list_of_doctors_who_pres_more_than_ten

