from department import Department
from subject import Subject
from student import Student
from student_subject import StudentSubject
from students import *

smer_1 = Department("smer_1","modul",[Subject("predmet1","A101"),Subject("predmet2","A102"),Subject("predmet3","A103"),
                                      Subject("predmet4","A104"),Subject("predmet5","A105")],[student_2,student_3])
smer_2 = Department("smer_2","modul",[Subject("predmet1","A101"), Subject("predmet2","A102"), Subject("predmet3","A103"),
                                      Subject("predmet4","A104"), Subject("predmet5","A105")],[student_1,student_4])
smer_3 = Department("smer_3","modul",[Subject("predmet1","A101"), Subject("predmet2","A102"), Subject("predmet3","A103"),
                                      Subject("predmet4","A104"), Subject("predmet5","A105")],[student_8])
smer_4 = Department("smer_4","modul",[Subject("predmet1","A101"), Subject("predmet2","A102"), Subject("predmet3","A103"),
                                      Subject("predmet4","A104"), Subject("predmet5","A105")],[student_5])
smer_5 = Department("smer_5","modul",[Subject("predmet1","A101"), Subject("predmet2","A102"), Subject("predmet3","A103"),
                                      Subject("predmet4","A104"), Subject("predmet5","A105")],[student_6,student_9,student_10])
smer_6 = Department("smer_6","modul",[Subject("predmet1","A101"), Subject("predmet2","A102"), Subject("predmet3","A103"),
                                      Subject("predmet4","A104"), Subject("predmet5","A105")],[student_7,student_11])


departments_list=[smer_1, smer_2, smer_3, smer_4, smer_5, smer_6]

def display_all_departments(departments_list):
    display=""
    for i in range(len(departments_list)):
        display += str(i+1)+":"+departments_list[i].name+" <<>> "
    return display

