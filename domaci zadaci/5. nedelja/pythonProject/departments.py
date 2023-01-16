from department import Department
from subject import Subject

smer_1 = Department("energetika","elektrotehnicki odseci",[Subject("predmet1","100"), Subject("predmet2","200"), Subject("predmet3","300"), Subject("predmet4","400"), Subject("predmet5","500")],[])
smer_2 = Department("telekomunikacije","elektrotehnicki odseci",[Subject("predmet1","100"), Subject("predmet2","200"), Subject("predmet3","300"), Subject("predmet4","400"), Subject("predmet5","500")],[])
smer_3 = Department("elektronika","elektrotehnicki odseci",[Subject("predmet1","100"), Subject("predmet2","200"), Subject("predmet3","300"), Subject("predmet4","400"), Subject("predmet5","500")],[])
smer_4 = Department("racunarska tehnika i informatika","elektrotehnicki odseci",[Subject("predmet1","100"), Subject("predmet2","200"), Subject("predmet3","300"), Subject("predmet4","400"), Subject("predmet5","500")],[])
smer_5 = Department("fizicka elektronika","elektrotehnicki odseci",[Subject("predmet1","100"), Subject("predmet2","200"), Subject("predmet3","300"), Subject("predmet4","400"), Subject("predmet5","500")],[])
smer_6 = Department("signali i sistemi","elektrotehnicki odseci",[Subject("predmet1","100"), Subject("predmet2","200"), Subject("predmet3","300"), Subject("predmet4","400"), Subject("predmet5","500")],[])
department_list=[smer_1,smer_2,smer_3,smer_4,smer_5,smer_6]

def diplay_all_departments(department_list):
    display=""
    for i in range(len(department_list)):
        display += str(i+1)+":"+department_list[i].name+" <<>> "
    return display
