import typing as t
from student import Student
from subject import Subject

class Department:

    def __init__(self,name: str,module: str, subjects: t.List[Subject]=[], students:t.List[Student]=[]):
        self.name = name
        self.module = module
        self.subjects = subjects
        self.students = students

    def find_student_by_index(self,index:str):
        for student in self.students:
            if student.index_number==index:
                return student
            else:
                return None

    def add_subject_to_department(self, new_subject:t.List[str]):
        for subject in self.subjects:
            if subject==new_subject:
                print("That subject is already in this department")
                break
            else:
                self.subjects.append(new_subject)
                return self.subjects

    def add_student_to_department(self,new_student:Student):
        for student in self.students:
            if student.index_number==new_student.index_number:
                print("That student is already on this department")
                break
        else:
            self.students.append(new_student)
            return self.students

    def __str__(self):
        for i in range(len(self.students)):
            self.students[i]=self.students[i].__str__()
        for i in range(len(self.subjects)):
            self.subjects[i] = self.subjects[i].__str__()
        return f"{self.name}, {self.module}, {self.subjects}, {self.students}"
