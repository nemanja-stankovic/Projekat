import typing as t
from subject import Subject

class Student:

    def __init__(self,name: str,surname: str,index_number: str,department: str, subjects:t.List[dict]=[]):
        self.name=name
        self.surname=surname
        self.index_number=index_number
        self.department=department
        self.subjects=subjects

    def __str__(self):
        return f"{self.name} {self.surname}, {self.index_number}, {self.department}, {self.subjects}"