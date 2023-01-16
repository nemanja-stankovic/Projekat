from company import Company
from employee import Employee

if __name__ == '__main__':
    employee_1 = Employee("Marko", "Markovic", "0505979710545", 800, "senior developer")
    employee_2 = Employee("Žarko", "Žarkovic", "0606983710595", 800, "senior developer")
    employee_3 = Employee("Petar", "Petrovic", "0706988710454122", 600, "junior developer")
    employee_4 = Employee("Milica", "Milic", "0706988710454122", 950, "IT manager")
    employee_5 = Employee("Marija", "Markovic", "0706988710454122", 600, "junior developer")
    employee_6 = Employee("Milos", "Milosevic", "1708988790454127", 950, "IT manager")
    employee_7 = Employee("Nemanja", "Stankovic", "0705989710080", 600, "junior developer")

    list_of_employees = [employee_1, employee_2, employee_3, employee_4, employee_5, employee_6]
    """Creating initial list of employees in the company."""
    monty_development = Company("108754", "Monty Development d.o.o", list_of_employees)
    """Creating company."""
    print(monty_development.name)
    """Printing company name"""
    print([monty_development.employees[i].name for i in range(len(monty_development.employees))])
    """Printing company employees names"""
    monty_development.hire_employee(employee_7)
    """Hiring employee Nemanja"""
    print([monty_development.employees[i].name for i in range(len(monty_development.employees))])
    """Printing company employees names again"""
    monty_development.hire_employee(employee_7)
    """Trying to hire an employee that we already employed"""
    monty_development.fire_employee(employee_7)
    """Firing an employee"""
    print([monty_development.employees[i].name for i in range(len(monty_development.employees))])
    """Printing company employees names again"""
    monty_development.fire_employee(employee_7)
    """Trying to fire an employee that we don"t have"""
    monty_development.display_positions()
    """Printing company employees names again"""
    employee_7.change_hourly(620)
    """Changing hourly rate of an employee"""
    print(employee_7.hourly)
    """Printing hourly to check"""