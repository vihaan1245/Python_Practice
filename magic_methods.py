# class Example:
#     def __init__(self,name):
#         self.name = name
#         print(f"Hello {self.name}")
#
#     # def __new__(cls):
#     #     print("Hello World")
#     #     return super(Example,cls).__new__(cls)
#
# example1 = Example("Vihaan")
# print(example1)

class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __str__(self):
        return f"X:{self.x} and Y:{self.y} and Z:{self.z}"

vector1 = vector(2,5,10)
vector2 = vector(6,7,10)
sum_vector = vector1+vector2
print(sum_vector)