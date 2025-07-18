# Train Carriage Management (Doubly Linked List)
# Scenario:
# A train is modeled with carriages connected in a line. Each carriage has a unique number. The train can attach or detach carriages from both the front and the rear.
#
# Task:
#
# Implement a Train class using a doubly linked list.
# Create methods to:
# Attach a carriage at the front (attach_front(number)).
# Attach a carriage at the rear (attach_rear(number)).
# Detach a carriage from the front (detach_front()).
# Detach a carriage from the rear (detach_rear()).
# Display the carriages from front to rear (display_train()).

class Node:
    def __init__(self, number):
        self.number = number
        self.next = None
        self.prev = None

class Train:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def attach_front(self, number):
        new_front = Node(number)
        if self.is_empty():
            self.head = new_front
            self.tail = self.head
        else:
            new_front.next = self.head
            self.head.prev = new_front
            self.head = new_front
        self.length += 1


    def attach_rear(self, number):
        new_rear = Node(number)
        if self.is_empty():
            self.head = new_rear
            self.tail = self.head
        else:
            new_rear.prev = self.tail
            self.tail.next = new_rear
            self.tail = new_rear
        self.length += 1

    def detach_front(self):
        if self.is_empty():
            print("Cannot detach.")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def detach_rear(self):
        if self.is_empty():
            print("Cannot detach. The train is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def display_train(self):
        if self.is_empty():
            print("Cannot display, there is nothing.")
        temp = self.head
        while temp:
            print(f"Carriage : {temp.number}",end=" -> ")
            temp = temp.next
        print()

metropolitan = Train()
metropolitan.attach_rear(4)
metropolitan.attach_front(1)
metropolitan.attach_front(2)
metropolitan.attach_front(3)
metropolitan.attach_rear(5)
metropolitan.detach_rear()
metropolitan.detach_front()
metropolitan.display_train()
