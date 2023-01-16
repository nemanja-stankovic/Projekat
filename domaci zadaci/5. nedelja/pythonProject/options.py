from student import Student
from department import Department
from students import list_of_students
from departments import department_list, diplay_all_departments

def option_A():

    dep = int(input(f"Insert department number\n{diplay_all_departments(department_list)}"))
    for i in range(len(department_list)):
        if dep == i + 1:
            nbr = i
            break
    else:
        print(f"Not a valid number of department, you must type number between 1 and {len(department_list)}")
        option_A()
    ind = input(f"Insert student index number")
    for student in list_of_students:
        if student.index_number == ind:
            new_student = student
            department_list[nbr].add_student_to_department(new_student)
            break
    else:
        print("That students is not in our list of students")
    print(department_list[nbr])

# def option_B():
