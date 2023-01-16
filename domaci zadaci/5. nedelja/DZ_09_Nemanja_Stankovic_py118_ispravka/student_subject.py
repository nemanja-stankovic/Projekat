class StudentSubject:

    def __init__(self,subject_name: str, subject_ID: str, grade: int):
        self.subject_name=subject_name
        self.subject_ID=subject_ID
        self.grade=grade

    def __repr__(self):
        return f"{self.subject_name},{self.subject_ID},{self.grade}"

    def is_passed(self):
        if self.grade>5:
            return True
        else:
            return False


