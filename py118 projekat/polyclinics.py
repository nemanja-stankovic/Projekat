import typing as t
from doctor import Doctor

class Polyclinic:

    def __init__(self,name: str,place: str,phone_number: str,list_of_doctors:t.List[Doctor]):
        self.name=name
        self.place=place
        self.phone_number=phone_number
        self.list_of_doctors=list_of_doctors


    def __repr__(self):
        return f"{self.name},{self.place},br. tel:{self.phone_number} {self.list_of_doctors}"



