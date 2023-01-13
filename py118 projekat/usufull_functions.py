from doctor import Doctor
import typing as t
from prescriptions import Prescription

def read_file(file_name: str) -> str:
    """
    `read_file` takes a file name as input and returns the contents of the file as a string

    :param file_name: The name of the file to read
    :type file_name: str
    :return: The text of the file.
    """

    with open(file_name,'r') as f:
        text=f.read()
    return text

def split_words(text: str)->t.List[list]:
    """
    It takes a string of text, splits it into lines, splits each line into words, and returns a list of lists of words

    :param text: str
    :type text: str
    :return: A list of lists.
    """
    lines=text.split("\n")
    word_list=[]
    for word in lines:
        line=word.split("/")
        if line!=[""]:
            word_list.append(line)
    return word_list

def split_words_by_slash(text: str)->list:
    """
    It takes a string and returns a list of words, where the words are separated by slashes

    :param text: the text to be split
    :type text: str
    :return: A list of words
    """
    word_list=text.split("/")
    for i in range(len(word_list)):
        if word_list[i]=="":
           word_list.pop(i)
    return word_list

def split_words_by_comma(word_list: list)->t.List[list]:
    """
    It takes a list of words, splits each word by commas, and returns a list of lists of words

    :param word_list: list
    :type word_list: list
    :return: A list of lists of words.
    """
    word_list_list=[]
    for word in word_list:
        list=word.split(",")
        if list!=[""]:
            word_list_list.append(list)
    return word_list_list

def find_doctor(list_of_doctors,ID)-> Doctor:
    """
    **Given a list of doctors and an ID number, return the doctor with that ID number.**

    The function takes two arguments: a list of doctors and an ID number. It returns a doctor

    :param list_of_doctors: a list of Doctor objects
    :param ID: the ID number of the doctor you want to find
    :return: The doctor with the ID number that matches the ID number that was inputted.
    """
    for doctor in list_of_doctors:
        if doctor.ID_number==ID:
            return doctor

def is_it_booked(list_of_list:t.List[list], polyclynic_phone_number: str, doctor_ID: str, apointment) -> bool:
    """
    It checks if a given apointment is booked in a given polyclynic by a given doctor

    :param list_of_list: a list of lists, each list is a row in the csv file
    :type list_of_list: t.List[list]
    :param polyclynic_phone_number: str
    :type polyclynic_phone_number: str
    :param doctor_ID: str
    :type doctor_ID: str
    :param apointment: str
    :return: True or False
    """
    if len(list_of_list)==0:
        return False
    for list in list_of_list:
        if list[1]==polyclynic_phone_number and list[2]==doctor_ID and list[0]==apointment and len(list)>0:
            return True
        else:
            return False

def is_patient_booked(list_of_list:t.List[list], polyclynic_phone_number: str, doctor_ID: str, patient_ID: str):
    """
    It takes a list of lists, a polyclynic phone number, a doctor ID and a patient ID as input and returns the booking ID if
    the patient is booked, otherwise it returns None

    :param list_of_list: a list of lists, each list is a row in the table
    :type list_of_list: t.List[list]
    :param polyclynic_phone_number: str
    :type polyclynic_phone_number: str
    :param doctor_ID: str
    :type doctor_ID: str
    :param patient_ID: str
    :type patient_ID: str
    :return: The function is_patient_booked returns the booking ID if the patient is booked, otherwise it returns None.
    """
    if len(list_of_list)==0:
        return None
    for list in list_of_list:
        if list[1]==polyclynic_phone_number and list[2]==doctor_ID and list[3]==patient_ID and len(list)>0:
            return list[0]
        else:
            return None

def find_apointment_date(list_of_list:t.List[list],patient_ID: str):
    """
    It takes a list of lists and a patient ID as input and returns the date of the appointment for the patient with the
    given ID

    :param list_of_list: a list of lists, where each list is a list of strings
    :type list_of_list: t.List[list]
    :param patient_ID: str
    :type patient_ID: str
    :return: The date of the appointment
    """
    for list in list_of_list:
        if list[3]==patient_ID:
            return list[0]
    else:
        return None

def find_polyclinic_number(list_of_list:t.List[list],patient_ID: str):
    """
    It takes a list of lists and a patient ID as input, and returns the polyclinic number of the patient if the patient ID
    is found in the list of lists, and returns None otherwise

    :param list_of_list: a list of lists, where each list is a row of the table
    :type list_of_list: t.List[list]
    :param patient_ID: the patient's ID
    :type patient_ID: str
    :return: The polyclinic number of the patient with the given ID.
    """
    for list in list_of_list:
        if list[3]==patient_ID:
            return list[1]
    else:
        return None

def find_doctor_ID(list_of_list:t.List[list],patient_ID: str):
    """
    It takes a list of lists and a patient ID as input, and returns the doctor ID of the patient if the patient ID is in the
    list of lists, and returns None if the patient ID is not in the list of lists

    :param list_of_list: a list of lists, where each list is a list of strings
    :type list_of_list: t.List[list]
    :param patient_ID: str
    :type patient_ID: str
    :return: The doctor ID of the patient
    """
    for list in list_of_list:
        if list[3]==patient_ID:
            return list[2]
    else:
        return None

def choice_prescription(word_list_medicines):
    """
    It takes a list of medicines and returns a string of the medicines with a number next to each one

    :param word_list_medicines: a list of medicines
    :return: A string of the medicines in the list.
    """
    text=""
    for i in range(len(word_list_medicines)):
        line=f"{i + 1}) ---- {word_list_medicines[i]}\n"
        text+=line
    return text

def eliminate_apointment(list:list,apointment_date: str,phone_number: str,doctor_ID: str, patient_ID):
    """
    This function takes a list of apointments, an apointment date, a phone number, a doctor ID, and a patient ID, and
    returns the list of apointments with the apointment with the given information removed

    :param list: list
    :type list: list
    :param apointment_date: the date of the apointment
    :type apointment_date: str
    :param phone_number: the phone number of the patient
    :type phone_number: str
    :param doctor_ID: the ID of the doctor
    :type doctor_ID: str
    :param patient_ID: the ID of the patient
    :return: The list of apointments
    """
    index=-1
    for i in range(len(list)):
        if list[i]==apointment_date+","+phone_number+","+doctor_ID+","+patient_ID:
            index=i
    if index!=-1:
        list.pop(index)
    return list

def find_available_patient_ID(list_of_patients:list)-> str:
    """
    This function takes a list of patients and returns the next available patient ID number

    :param list_of_patients: a list of Patient objects
    :type list_of_patients: list
    :return: the available number for the patient ID.
    """
    available_number=str(1001+len(list_of_patients))
    return available_number

def find_medicine_by_code(word_list_medicines,code)->Prescription:
    """
    It takes a list of medicines and a code, and returns a prescription object with the code, name and price of the medicine

    :param word_list_medicines: a list of lists, each sublist is a medicine with its code, name and price
    :param code: the code of the medicine
    :return: A prescription object
    """
    for medicine in word_list_medicines:
        if medicine[0]==code:
            prescription=Prescription(medicine[0],medicine[1],medicine[2])
            return prescription