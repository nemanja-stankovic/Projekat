"""Model for Employee."""

from employee_datetime import HOURS_PER_DAY, DAYS_PER_MONTH, MONTHS_PER_YEAR


class Employee:
    """Model of instance Employee."""

    def __init__(self, name: str, surname: str, jmbg: str, hourly: int, position: str):
        """Initialize the Employee object."""
        self.name = name
        self.surname = surname
        self.jmbg = jmbg
        self.hourly = hourly
        self.position = position

    def calculate_monthly_income(self):
        """Calculate monthly income for given employee."""
        return self.hourly * HOURS_PER_DAY * DAYS_PER_MONTH

    def calculate_annual_income(self):
        """Calculate annual income for given employee."""
        return self.calculate_monthly_income() * MONTHS_PER_YEAR

    def change_hourly(self,new_hourly):
        """increase or reduce hourly rate"""
        self.hourly=new_hourly





