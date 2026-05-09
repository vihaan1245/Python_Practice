class employee():
    def __init__(self,name,age,work_hours):
        self.name = name
        self._age = age
        self.__work_hours = work_hours

    def __str__(self):
        return f"The Employee name is {self.name} \nThe Employee's age is {self._age} \nThe amount of hours worked are {self.__work_hours}"

    def learn(self):
        print(f"{self.name} is learning programming.")

employee1 = (employee("Vihaan",14, "8 hours"))
print(employee1.name)
print(employee1._age)
print(employee1._employee__work_hours)
print(employee1)
employee1.learn()

