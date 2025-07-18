from typing import List

from oops import employee


class Employee():
    def __init__(self,name,age,work_hours):
        self.name = name
        self.age = age
        self.work_hours = work_hours

    def __str__(self):
        return f"The Employee name is {self.name} \nThe Employee's age is {self.age} \nThe amount of hours worked are {self.work_hours}"

    def learn(self):
        print(f"{self.name} is learning programming.")


class Manager(Employee):
    def __init__(self, department: str, name, age, work_hours, employees: List[str] = None):
        super().__init__(name, age, work_hours)
        self.department = department
        self.employees = list(employees) if employees else []

    def add_employee(self,name:str) -> List[str]:
        if name not in self.employees:
            self.employees.append(name)
        else:
            print("Already in the roaster.")

        return self.employees

    def remove_employee(self,name):
        if name in self.employees:
            self.employees.remove(name)
            print(f"Employee removed is {name}")
        else:
            print(f"The employee has already been removed or does not exist")

        return self.employees

    def print_employees(self):
        for employee in self.employees:
            print(employee, "-")

class Ceo(Manager):
    def __init__(self, department: str, name, age, work_hours,employees: List[str], company_name, list_managers: List[str]):
        super().__init__(department, name, age, work_hours, employees)
        self.company_name = company_name
        self.list_managers = list(list_managers) if list_managers else []

    def company_name(self):
        print(f"The company name is {self.company_name}")

    def print_managers(self):
        for managers in self.list_managers:
            print(managers)

# manager = Manager("Marketing","Vihaan","38","2",["Suhaan","John","Adan","Ahaan","Mike"])
# manager.print_employees()

ceo = Ceo("Head", "Random", 14, 5, ["Suhaan","John","Adan","Ahaan","Mike"], "Marketing Head department", ["Vihaan","x","Y","Z"])
ceo.print_managers()






