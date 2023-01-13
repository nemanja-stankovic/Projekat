from appointment_time import *
from options import *


def save_file_apointment_list(list_of_apointments):
    with open("zakazani_pregledi.txt",'w+') as f:
        text=""
        for apointment in list_of_apointments:
            line=f"{apointment}/"
            if line!="/":
                text+=line
        f.write(text)

def add_patient_to_file(file_name,name: str,surname: str,phone_number: str,patient_ID: str,doctor_ID: str,adress: str):
    with open(file_name,"a") as f:
        f.write(f"/{patient_ID}/{name}/{surname}/{adress}/{phone_number}/{doctor_ID}")

def save_examinations(list_of_examinations: list):
    with open("pregledi.txt",'w+') as f:
        text = ""
        for examination in list_of_examinations:
            examination_str=examination.show_examination()
            line=f"{examination_str}/"
            if line != "/":
                text += line
        f.write(text)
