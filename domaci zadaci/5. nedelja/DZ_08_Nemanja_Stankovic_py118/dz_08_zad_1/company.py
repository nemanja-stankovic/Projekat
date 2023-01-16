"""Model for describing companies."""

import typing as t
from employee import Employee


class Company:
    """Model for company."""

    def __init__(self, pib: str, name: str, employees: t.List[Employee] = []):
        """Initialize the Company object."""
        self.pib = pib
        self.name = name
        self.employees = employees

    def hire_employee(self, employee: Employee):
        """Hire an employee."""
        if self.find_employee_by_jmbg(employee.jmbg)!= employee:
            self.employees.append(employee)
        else:
            print("We already have that employee employed!")

    def fire_employee(self,employee:Employee):
        """Fire an employee."""
        index=-1
        for i in range(len(self.employees)):
            if employee.jmbg==self.employees[i].jmbg:
                index=i
        if index==-1:
            print("You don't have that employee")
        else:
            self.employees.pop(i)

    def find_employee_by_jmbg(self, jmbg: str):
        """Find employee by jmbg if exists in list of employees."""
        for e in self.employees:
            if e.jmbg == jmbg:
                return e
        return None

    def display_positions(self):
        """Displaying all positions in the company."""
        positions_list=[]
        for e in self.employees:
            positions_list.append(e.position)
        print(set(positions_list))

