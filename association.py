class Vehicle:
    def __init__(self,model,brand,price,engine):
        self.model = model
        self.brand = brand
        self.price = price
        self.engine = engine

class Engine:
    def __init__(self,horsepower,fuel,type):
        self.type = type
        self.fuel = fuel
        self.horsepower = horsepower

bmw_engine = Engine(5000, "diesel","engine-76931")
BMW = Vehicle("benz","BMW","150000",bmw_engine)
print(BMW.engine.horsepower)

class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None

obj_1 = Node(10)
obj_2 = Node(20)
obj_3 = Node(30)

obj_1.next = obj_2
obj_2.next = obj_3
print(obj_1.next.next.data)

