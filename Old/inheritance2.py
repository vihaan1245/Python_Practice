class Mammals:
    pass

class Animal(Mammals):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def run(self):
        print(f"{self.name} can run")

    def test(self):
        print("I am inside the animal class.")

class Dog(Animal):
    def __init__(self, name, size, breed):
        super().__init__(name, size)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, size,sound):
        super().__init__(name, size)
        self.sound = sound



class Aerial(Mammals):
    def __init__(self,colour, flying_time,name):
        self.flying_time = flying_time
        self.colour = colour
        self.name = name

    def fly(self):
        print(f"{self.name} can fly")

    def test(self):
        print("I am inside the Aerial class")

class Bird(Animal,Aerial):
    def __init__(self, colour, flying_time,name):
        super().__init__(colour, flying_time,name)

crow = Bird("Black","30 minutes","Amop")
crow.fly()
crow.run()
crow.test()


