
class Patient:

    def __init__(self,name: str,surname: str,phone_number: str,patient_ID: str,doctor_ID: str,adress: str=""):
        self.name=name
        self.surname=surname
        self.phone_number=phone_number
        self.patient_ID = patient_ID
        self.doctor_ID=doctor_ID
        self.adress=adress


    def __repr__(self):
        return f"br.kartona: {self.patient_ID}, {self.name} {self.surname}, telefon:{self.phone_number},adresa:{self.adress}"
