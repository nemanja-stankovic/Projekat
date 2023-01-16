from student import Student
from department import Department
from departments import departments_list,display_all_departments
from subject import Subject
from student_subject import StudentSubject
from options import option_A ,option_B, option_C, option_D, option_E, option_F, option_G, option_H, option_I, option_J, option_K, option_L, option_M
from students import list_of_students

def main():
    unos=""
    while unos!="Z":
        unos=input("Enter option\n"
                   "A - add new student to department\n"
                   "B.- add new subject to department\n"
                   "C - add new subject to student\n"
                   "D - show list of all passed student exams\n"
                   "E - show average grade of student\n"
                   "F - show student/s info that have highest average grade\n"
                   "G - show student/s info  with least passed exams \n"
                   "H - show all students who have passed all exams in the subjects assigned to them\n"
                   "I - division of students by departments in percentage\n"
                   "J - show all students in the chosen department\n"
                   "K - best student at chosen department\n"
                   "L - show all subjects that no student has passed\n"
                   "M - show subject with highest average grade\n"
                   "Z - end of program\n ").upper()
        if unos=="A":
            option_A()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos="Z"
        elif unos=="B":
            option_B()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos=="C":
            option_C()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "D":
            option_D()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "E":
            option_E()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "F":
            option_F()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "G":
            option_G()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "H":
            option_H()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "I":
            option_I()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "J":
            option_J()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "K":
            option_K()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "L":
            option_L()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"
        elif unos == "M":
            option_M()
            u=input("Press any key to return to main meni or Z to end\n").upper()
            if u!="Z":
                continue
            else:
                unos = "Z"



if __name__ == '__main__':
    main()
