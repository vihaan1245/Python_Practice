class Stack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = [None]*self.capacity
        self.top = -1

    def push(self,value):
        if self.is_full:
            print("It is full")
            return None
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty:
            print("There is nothing")
            return None
        temp = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return temp

    def peek(self):
        if self.is_empty:
            print("There is nothing")
            return None
        return self.stack[self.top]

    @property
    def is_empty(self):
        return self.top == -1

    @property
    def is_full(self):
        return self.top == self.capacity-1

    def display(self):
        for i in range(self.top + 1):
            print(self.stack[i])

books = Stack(10)
books.push("Harry potter")
books.push("Rizzard of OZ")
books.push("Skibidi Sigmas")
books.display()
