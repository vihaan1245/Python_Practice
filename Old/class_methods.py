class person:
    school = "Oberoi International School"
    def __init__(self,name):
        self.name = name

    #Instant method
    def display_name(self):
        return self.name

    #Class method
    @classmethod
    def update_school(cls,schoolname):
        cls.school = schoolname
        cls.address = "Bangalore"

    #Static Method
    @staticmethod
    def calc_salary(salary):
        return salary*0.75

person1 = person("Vihaan")
person2 = person("Suhaan")
person.update_school("Podar")
print(person1.calc_salary(100009))
print(person1.name)
print(person2.name)
print(person1.school)
print(person2.school,person2.address)