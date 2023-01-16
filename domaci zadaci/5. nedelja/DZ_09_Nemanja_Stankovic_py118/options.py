from student import Student
from department import Department
from students import list_of_students
from departments import departments_list, display_all_departments

def option_A():

    dep = int(input(f"Insert department number\n{display_all_departments(departments_list)}"))
    for i in range(len(departments_list)):
        if dep == i + 1:
            nbr = i
            break
    else:
        print(f"Not a valid number of department, you must type number between 1 and {len(departments_list)}")
        option_A()
    ind = input(f"Insert student index number")
    for student in list_of_students:
        if student.index_number == ind:
            new_student = student
            departments_list[nbr].add_student_to_department(new_student)
            break
    else:
        print("That students is not in our list of students")
    print(departments_list[nbr])

def option_B():
    dep = int(input(f"Insert department number\n{display_all_departments(departments_list)}"))
    for i in range(len(departments_list)):
        if dep == i + 1:
            nbr = i
            break
    else:
        print(f"Not a valid number of department, you must type number between 1 and {len(departments_list)}")
        option_B()
    sub = input(f"Insert subject ID")
    for department in departments_list:
        for subject in department.subjects:
            if subject.subject_ID == sub:
                new_subject=subject
            department.add_subject_to_department(new_subject)
        else:
            break
    else:
        print("That subject is not in our list of subjects")
    print(departments_list[nbr])