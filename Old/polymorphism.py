# #Overloading
# def add(x,y):
#     return x+y
#
# sum = add(12,8)
# print(sum)
#
# def add(x,y,z):
#     return x+y+z
#
# sum1 = add(5,6,9)
# print(sum1)
# print(1+2)
# print("Hello" + " Vihaan")
#
# #Operator overloading
# class A:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, others):
#         return self.a + others.a, self.b + others.b
#
# obj1 = A(5,5)
# obj2 = A(6,6)
# print(obj2+obj1)

#Overwriting
# class F1:
#     def run(self):
#         print("Win")
#
# class F2(F1):
#     def run(self):
#         print("Second place")
#
#     def run(self,a=8):
#         print(a)
#
# driver1 = F1()
# driver1.run()
# driver2 = F2()
# driver2.run()

#Polymorphism using duck typing
class Car:
    def start(self):
        print("Car is starting....")

class Truck:
    def start(self):
        print("Truck is starting....")

class Bus:
    def stop(self):
        print("Bus is stopping....")

vehicle = [Car(), Truck(), Bus()]
print(type(vehicle))

for v in vehicle:
    v.start()
