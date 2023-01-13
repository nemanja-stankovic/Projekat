

class Prescription:

    def __init__(self, code: str,medicine_name:str, way_of_using: str):
        self.code=code
        self.medicine_name=medicine_name
        self.way_of_using=way_of_using

    def __repr__(self):
        return f"{self.code} {self.medicine_name}, {self.way_of_using}"

