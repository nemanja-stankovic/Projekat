from student import Student
from department import Department
from subject import Subject
from students import *
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
    new_student=0
    for student in list_of_students:
        if student.index_number == ind:
            new_student = student
            departments_list[nbr].add_student_to_department(new_student)
            break
    else:
        print("That students is not in our list of students")
    if new_student==0:
        print(departments_list[nbr])


def option_B():

    dep = int(input(f"Insert department number\n{display_all_departments(departments_list)}"))
    nbr=len(departments_list)+1
    for i in range(len(departments_list)):
        if dep == i + 1:
            nbr = i
    if nbr==len(departments_list)+1:
        print(f"Not a valid number of department, you must type number between 1 and {len(departments_list)}")
        option_B()
    sub_ID = input(f"Insert subject ID")
    sub_name=input(f"Insert subject name")
    new_subject=Subject(sub_name,sub_ID)
    departments_list[nbr].add_subject_to_department(new_subject)
    print(departments_list[nbr])

def option_C():
    ind = input(f"Insert student index number")
    sub_ID = input(f"Insert subject ID")
    sub_name = input(f"Insert subject name")
    new_subject = Subject(sub_name, sub_ID)

    for student in list_of_students:
        if student.index_number == ind:
            student.add_new_subject(new_subject)
            print(student)
            break
    else:
        print("That student is not in our list of students")


def option_D():
    ind = input(f"Insert student index number")
    for student in list_of_students:
        if student.index_number == ind:
            print(f"List of all passed subjects of student: {student.name} {student.surname} is {student.all_passed_subjects()}")
            break
    else:
        print("Student with that index number is not in our list of students")

def option_E():
    ind = input(f"Insert student index number")
    for student in list_of_students:
        if student.index_number == ind:
            print(f"Student {student.name} {student.surname} average grade is {student.average_grade()}")
            break
    else:
        print("Student with that index number is not in our list of students")

def option_F():
    max_avg_grade=0
    index_max_avg_grade=""
    list_best_students=[]
    for student in list_of_students:
        if student.average_grade()>max_avg_grade:
            max_avg_grade=student.average_grade()
            index_max_avg_grade=student.index_number
            best_student=student
    list_best_students.append(best_student)
    print("Students with highest average grade are:")
    for student in list_of_students:
        if student.average_grade() == max_avg_grade and student.index_number!=index_max_avg_grade:
            list_best_students.append(student)
    for student in list_best_students:
        print(f"{student.name} {student.surname},{student.index_number},average grade:{student.average_grade()}")

def option_G():
    min_number_of_passed=0
    index_worst_students=""
    for student in list_of_students:
        min_number_of_passed += len(student.subjects)
    list_worst_students=[]
    for student in list_of_students:
        if len(student.all_passed_subjects())<min_number_of_passed:
            min_number_of_passed=len(student.all_passed_subjects())
            index_worst_students=student.index_number
            worst_student=student
    list_worst_students.append(worst_student)
    for student in list_of_students:
        if len(student.all_passed_subjects()) == min_number_of_passed and index_worst_students!=student.index_number:
            list_worst_students.append(student)
    print(f"Students with least passed exams are:\n{list_worst_students}")

def option_H():
    list_students_who_passed_all=[]
    for student in list_of_students:
        if len(student.subjects)==len(student.all_passed_subjects()):
            list_students_who_passed_all.append(student)
    if len(list_students_who_passed_all)==0:
        print("No student passed all exams")
    else:
        print(f"Students who all passed exams are {list_students_who_passed_all}")

def option_I():
    number_of_all_students=0
    for departman in departments_list:
        number_of_all_students+=departman.number_of_students()
    for departman in departments_list:
        print(f"{departman.name}: {round(100*departman.number_of_students()/number_of_all_students,2)}%")

def option_J():
    dep = int(input(f"Insert department number\n{display_all_departments(departments_list)}"))
    for i in range(len(departments_list)):
        if dep == i + 1:
            nbr = i
            break
    else:
        print(f"Not a valid number of department, you must type number between 1 and {len(departments_list)}")
        option_J()
    print(f"All students at this department are:{departments_list[nbr].all_students()}")

def option_K():
    dep = int(input(f"Insert department number\n{display_all_departments(departments_list)}"))
    for i in range(len(departments_list)):
        if dep == i + 1:
            nbr = i
            break
    else:
        print(f"Not a valid number of department, you must type number between 1 and {len(departments_list)}")
        option_K()
    print("Best students at this department are:")
    departments_list[nbr].best_students()

def option_L():
    list_of_passed=[]
    list_of_failed=[]
    list_of_grades=[]
    all_failed=[]
    for student in list_of_students:
        for subject in student.subjects:
            if subject.is_passed():
                list_of_passed.append(subject.subject_name)
                list_of_grades.append(subject.grade)
            else:
                list_of_failed.append(subject.subject_name)
    for subject in list_of_failed:
        if subject not in list_of_passed:
            all_failed.append(subject)
    all_failed=set(all_failed)
    print(f"Subjects that no student has passed are {all_failed}")

def option_M():
    highest_avg=5
    list_of_subjects=[]
    list_of_grades=[]
    for student in list_of_students:
        for subject in student.subjects:
            list_of_subjects.append(subject.subject_name)
            list_of_grades.append(subject.grade)
    for i in range(len(list_of_subjects)):
        num=1
        for j in range(len(list_of_subjects)):
            if list_of_subjects[i]==list_of_subjects[j] and j>i:
                list_of_grades[i]+=list_of_grades[j]
                num+=1
        list_of_grades[i]=list_of_grades[i]/num
    max_grade=0
    index_max=0
    for i in range(len(list_of_subjects)):
        if list_of_grades[i]>max_grade:
            max_grade=list_of_grades[i]
            index_max=i
    print(f"Subject with highest avg grade is: {list_of_subjects[index_max]}, with avg grade {round(list_of_grades[index_max], 2)}")


