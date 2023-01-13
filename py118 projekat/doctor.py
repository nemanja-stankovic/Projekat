
class Doctor:

    def __init__(self,name: str, surname: str, ID_number: str, phone_number: str,specialty: str):
        self.name=name
        self.surname=surname
        self.ID_number=ID_number
        self.phone_number=phone_number
        self.specialty=specialty

    def __repr__(self):
        return f"{self.name} {self.surname},ID:{self.ID_number},{self.specialty}"


