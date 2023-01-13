from patients import Patient
from doctor import Doctor
from polyclinics import Polyclinic
from prescriptions import Prescription

class Examination:

    def __init__(self,polyclinic:Polyclinic,patient:Patient,doctor:Doctor,diagnose: str,prescription: Prescription, examination_date: str ):
        self.patient=patient
        self.doctor=doctor
        self.diagnose=diagnose
        self.prescription=prescription
        self.polyclinic=polyclinic
        self.examination_date=examination_date

    def __repr__(self):
        return f"pacijent {self.patient.name} {self.patient.surname} pregledan od strane dr {self.doctor}, dana {self.examination_date} i postavio dijagnozu: {self.diagnose} i prepisao sledeci lek {self.prescription}"


    def show_examination(self):
        return f"{self.patient.patient_ID}/{self.doctor.ID_number}/{self.diagnose}/{self.prescription.code}/{self.examination_date}/{self.polyclinic.phone_number}"