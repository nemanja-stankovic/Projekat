import typing as t
from student_subject import StudentSubject

class Student:

    def __init__(self,name: str,surname: str,index_number: str,department: str, subjects:t.List[StudentSubject]=[]):
        self.name=name
        self.surname=surname
        self.index_number=index_number
        self.department=department
        self.subjects=subjects

    def add_new_subject(self,new_subject:StudentSubject):
        for subject in self.subjects:
            if subject.subject_ID == new_subject.subject_ID:
                print("Student already has subject with that subject ID")
                break
        else:
            self.subjects.append(new_subject)
        return self.subjects

    def all_passed_subjects(self):
        all_passed_subjects=[]
        for subject in self.subjects:
            if subject.grade>5:
                all_passed_subjects.append(subject)
        return all_passed_subjects

    def average_grade(self):
        sum_of_grades=0
        for subject in self.all_passed_subjects():
            sum_of_grades+=subject.grade
        average_grade=sum_of_grades/len(self.all_passed_subjects())
        return average_grade



    def __repr__(self):
        for i in range(len(self.subjects)):
            self.subjects[i] = self.subjects[i].__str__()
        return f"{self.name} {self.surname}, {self.index_number}, {self.department}, {self.subjects}"
