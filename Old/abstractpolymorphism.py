from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,model,maker,color):
        self.model = model
        self.maker = maker
        self.color = color

    @abstractmethod
    def move_forward(self):
        raise NotImplementedError("This method is not applied the same for both vehicles my cuh.")

class Car(Vehicle):
    def __init__(self, model, maker, color):
        super().__init__(model, maker, color)

    def start(self):
        print("Car is starting....")

    def move_forward(self):
        print("The car is moving forward using accelerator....")

class Bike(Vehicle):
    def __init__(self, model, maker, color):
        super().__init__(model, maker, color)

    def move_forward(self):
        print("The bike is moving forward using handles....")

kawasaki = Bike("Kawasaki GTX-40", "Me","Blue")
mustang = Car("Mustang 1999 slim edition benz", "Me again","Grey and Black")
mustang.move_forward()
kawasaki.move_forward()

